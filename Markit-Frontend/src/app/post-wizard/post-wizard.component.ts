import {AfterViewInit, ChangeDetectorRef, Component, OnInit, ViewChild} from '@angular/core';
import {Location} from '@angular/common';
import {ActivatedRoute, Router} from '@angular/router';
import {CalendarService, PostService, TwitterService} from '@services';
import {MatSnackBar} from '@angular/material';
import {CalendarDetailsFormComponent} from '@app/calendar-details-form/calendar-details-form.component';
import {PostDetailsFormComponent} from '@app/post-details-form/post-details-form.component';
import {BasePostContentComponent} from '@app/base-post-content/base-post-content.component';
import {Calendar, Post} from '@models';
import {SocialChannelsSelectionComponent} from '@app/social-channels-selection/social-channels-selection.component';

@Component({
  selector: 'app-post-wizard',
  templateUrl: './post-wizard.component.html',
  styleUrls: ['./post-wizard.component.scss']
})
export class PostWizardComponent implements OnInit, AfterViewInit {
  @ViewChild('post_general_info', {static: false}) postGeneralInfo: PostDetailsFormComponent;
  @ViewChild('post_content', {static: false}) postContent: BasePostContentComponent;
  @ViewChild('post_channels', {static: false}) postChannels: SocialChannelsSelectionComponent;

  calendarId: number;
  calendar: Calendar = null;
  postId: number;
  post: Post = null;
  loading = false;

  constructor(private location: Location,
              private route: ActivatedRoute,
              private router: Router,
              private postService: PostService,
              private calendarService: CalendarService,
              private twitterService: TwitterService,
              private snackBar: MatSnackBar) {
  }

  get canPublish(): boolean {
    return this.postChannels ? this.postChannels.twitterEnabled : false;
  }

  ngOnInit(): void {
    this.calendarId = +this.route.snapshot.paramMap.get('calendarId');

    if (this.location.isCurrentPathEqualTo(`calendars/${this.calendarId}/posts/new`)) {
      return;
    }

    this.postId = +this.route.snapshot.paramMap.get('postId');
  }

  ngAfterViewInit() {
    this.calendarService.get(this.calendarId).subscribe((value: Calendar) => {
      console.log('calendar: ', value);
      this.calendar = value;
      if (this.postId) {
        this.postService.get(this.postId).subscribe((v: Post) => {
          console.log(v);

          this.post = v;
          this.postGeneralInfo.form.controls.subject.setValue(this.post.subject);
          this.postContent.form.controls.text.setValue(this.post.text);
          this.postContent.imageUrl = this.post.image;
          this.postChannels.connectedPlatforms = this.calendar.connectedPlatforms.split('/');
        }, err => {
          console.log(err);
          this.router.navigate(['/calendars', this.calendarId, 'posts', 'new']);
        });
      }
    }, err => {
      console.log(err);
      this.snackBar.open('Calendar not found!', 'Dismiss', {duration: 2000});
      this.router.navigate(['/']);
    });
  }

  createPost(publish: boolean = false, schedule: boolean = false) {
    this.loading = true;

    const postData = new FormData();
    postData.append('calendar', `${this.calendarId}`);
    if (this.postContent.selectedFile) {
      postData.append('image', this.postContent.selectedFile, this.postContent.selectedFile.name);
    }
    postData.append('subject', this.postGeneralInfo.form.controls.subject.value);
    postData.append('text', this.postContent.form.controls.text.value);
    if (schedule) {
      postData.append('scheduledTime', this.postGeneralInfo.date.value);
    }

    this.postService.create(postData).subscribe(
      (value: Post) => {
        console.log(value);

        this.post = value;
        this.postId = value.id;

        this.snackBar.open('Post has been created successfully!', 'Dismiss', {duration: 2000});

        if (publish) {
          this.twitterService.publishTweet(this.post.id).subscribe(
            v => {
              this.snackBar.open('Post has been published', 'Dismiss', {duration: 2000});
              console.log(v);
            }, e => {
              this.snackBar.open(`Failed to publish post`, 'Dismiss', {duration: 2000});
              console.log(e);
            }, () => {
              this.router.navigate(['/calendars', this.calendarId, 'posts']);
            }
          );
        } else {
          this.router.navigate(['/calendars', this.calendarId, 'posts']);
        }
      }, err => {
        console.log(err);

        this.loading = false;
        this.snackBar.open('Post creation failed!', 'Dismiss', {duration: 2000});
      }
    );
  }

  updatePost() {  // todo patch mode update
    this.loading = true;

    const updatedPostData = new FormData();
    // updatedPostData.append('calendar', `${this.calendarId}`);
    if (this.postContent.selectedFile) {
      updatedPostData.append('image', this.postContent.selectedFile, this.postContent.selectedFile.name);
    }
    updatedPostData.append('image', this.postContent.selectedFile, this.postContent.selectedFile.name); // todo what???? diff upper line
    updatedPostData.append('subject', this.postGeneralInfo.form.controls.subject.value);
    updatedPostData.append('text', this.postContent.form.controls.text.value);

    this.postService.partialUpdate(this.post.id, updatedPostData).subscribe((value: Post) => {
        console.log(value);

        this.snackBar.open('Post has been updated successfully!', 'Dismiss', {duration: 1000});
        // this.loading = false;
        this.router.navigate(['/calendars', this.calendarId, 'posts']);
      }, err => {
        console.log(err);

        this.loading = false;
        this.snackBar.open('Post updating failed!', 'Dismiss', {duration: 1000});
      }
    );
  }

  schedulePost() {
    if (this.postId) {
      this.updatePost();
    } else {
      this.createPost(false, true);
    }
  }

  publishPost() {
    if (this.postId) {
      this.updatePost();
    } else {
      this.createPost(true);
    }
  }
}
