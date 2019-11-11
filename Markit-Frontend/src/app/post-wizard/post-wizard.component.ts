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

  private calendarId: number;
  private calendar: Calendar = null;
  private postId: number;
  private post: Post = null;
  private loading = false;

  constructor(private location: Location,
              private route: ActivatedRoute,
              private router: Router,
              private postService: PostService,
              private calendarService: CalendarService,
              private twitterService: TwitterService,
              private snackBar: MatSnackBar) {
  }

  private get canPublish(): boolean {
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

  createPost() {
    this.loading = true;

    const postData = new FormData();
    postData.append('calendar', `${this.calendarId}`);
    postData.append('image', this.postContent.selectedFile, this.postContent.selectedFile.name);
    postData.append('subject', this.postGeneralInfo.form.controls.subject.value);
    postData.append('text', this.postContent.form.controls.text.value);

    this.postService.create(postData).subscribe(
      (value: Post) => {
        console.log(value);

        this.post = value;
        this.postId = value.id;
        this.snackBar.open('Post has been created successfully!', 'Dismiss', {duration: 2000});
        this.router.navigate(['/calendars', this.calendarId, 'posts']);
      }, err => {
        console.log(err);

        this.loading = false;
        this.snackBar.open('Post creation failed!', 'Dismiss', {duration: 2000});
      }
    );
  }

  updatePost() {
    this.loading = true;

    // const updatedPost: Post = this.post;

    const updatedPostData = new FormData();
    updatedPostData.append('calendar', `${this.calendarId}`);
    updatedPostData.append('image', this.postContent.selectedFile, this.postContent.selectedFile.name);
    updatedPostData.append('subject', this.postGeneralInfo.form.controls.subject.value);
    updatedPostData.append('text', this.postContent.form.controls.text.value);

    this.postService.update(updatedPostData).subscribe((value: Post) => {
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

  publishPost() {
    if (this.postId) {
      this.updatePost();
    } else {
      this.createPost();
    }

    this.twitterService.publishTweet(this.postId).subscribe(
      v => {
        console.log(v);
      }, e => {
        console.log(e);
      }
    );
  }
}
