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
  publishDateTime = '';

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
    this.calendarService.get(this.calendarId).subscribe((calendarResponse: Calendar) => {
      // console.log('calendar: ', calendarResponse);
      this.calendar = calendarResponse;

      if (this.postId) {
        this.postService.get(this.postId).subscribe((postResonse: Post) => {
          // console.log(postResonse);
          this.post = postResonse;
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

    const postData: FormData = this.createFormDataObject(schedule);
    postData.append('calendar', `${this.calendarId}`);
    // console.log(`post image: ${postData.get('image')}`);
    // console.log(`post subject: ${postData.get('subject')}`);
    // console.log(`post texy: ${postData.get('text')}`);
    // console.log(`post date: ${postData.get('publishDateTime')}`);

    if (postData) {
      this.postService.create(postData).subscribe(
        (postResponse: Post) => {
          this.post = postResponse;
          this.postId = postResponse.id;

          console.log(postResponse);
          this.snackBar.open('Post has been created successfully!', 'Dismiss', {duration: 2000});

          if (publish) {
            this.publishTweet();
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
  }


  updatePost(publish: boolean = false, schedule: boolean = false) {
    this.loading = true;

    const updatedPostData = this.createFormDataObject(schedule);

    if (updatedPostData) {
      this.postService.partialUpdate(this.post.id, updatedPostData).subscribe((postResponse: Post) => {
          console.log(postResponse);

          this.snackBar.open('Post has been updated successfully!', 'Dismiss', {duration: 1000});
          // this.loading = false;
          if (publish) {
            this.publishTweet();
          } else {
            this.router.navigate(['/calendars', this.calendarId, 'posts']);
          }
        }, err => {
          console.log(err);
          this.loading = false;
          this.snackBar.open('Post updating failed!', 'Dismiss', {duration: 1000});
        }
      );
    }
  }

  private createFormDataObject(schedule: boolean = false): FormData {
    const formData = new FormData();

    if (this.postContent.selectedFile) {
      formData.append('image', this.postContent.selectedFile, this.postContent.selectedFile.name);
    }
    formData.append('subject', this.postGeneralInfo.form.controls.subject.value);
    formData.append('text', this.postContent.form.controls.text.value);
    if (schedule) {
      if (this.standardizedTime()) {
        // console.log('final time', this.publishDateTime);
        formData.append('publishDateTime', this.publishDateTime);
      } else {
        return null;
      }
    }

    return formData;
  }

  private standardizedTime(): boolean {
    // console.log('now is:', this.postGeneralInfo.postDate.getFullYear(),
    //   this.postGeneralInfo.postDate.getMonth(),
    //   this.postGeneralInfo.postDate.getDate());
    // console.log('time hour form is:', this.postGeneralInfo.form.controls.time.value.getHours());
    // console.log('time minute form is:', this.postGeneralInfo.form.controls.time.value.getMinutes());
    // console.log('date is:', this.postGeneralInfo.form.controls.date.value);

    const postYear = this.postGeneralInfo.form.controls.date.value.getFullYear();
    let postMonth = this.postGeneralInfo.form.controls.date.value.getMonth() + 1;
    let postDay = this.postGeneralInfo.form.controls.date.value.getDate();
    let postHour = this.postGeneralInfo.form.controls.time.value.getHours();
    let postMinute = this.postGeneralInfo.form.controls.time.value.getMinutes();

    // ----------CHECK SCHEDULED TIME------------------
    const postDate = new Date(postYear, postMonth, postDay, postHour, postMinute, 0, 0);
    const TWO_MIN = 2 * 1000;
    // console.log(`${postDate.getTime()} - ${new Date().getTime()} = `, postDate.getTime() - new Date().getTime());
    if ((postDate.getTime() - new Date().getTime()) < TWO_MIN) {
      this.snackBar.open(`The scheduled time should at least be 2 minutes later!`, 'Dismiss', {duration: 2000});
      console.log('The scheduled time should at least be 2 minutes later!');
      return false;
    }

    // Add 0 before date, month, hrs or mins if they are less than 0
    postDay = postDay < 10 ? '0' + postDay : postDay;
    postMonth = postMonth < 10 ? '0' + postMonth : postMonth;
    postHour = postHour < 10 ? '0' + postHour : postHour;
    postMinute = postMinute < 10 ? '0' + postMinute : postMinute;

    // ----------TIMEZONE----------
    const timezoneOffsetMinute = new Date().getTimezoneOffset();
    let offsetHour = `${parseInt(String(Math.abs(timezoneOffsetMinute / 60)), 10)}`;
    let offsetMinute = `${Math.abs(timezoneOffsetMinute % 60)}`;
    let timezoneStandard;

    offsetHour = +offsetHour < 10 ? '0' + offsetHour : offsetHour;
    offsetMinute = +offsetMinute < 10 ? '0' + offsetMinute : offsetMinute;

    // Add an opposite sign to the offset, If offset is 0, it means timezone is UTC
    if (timezoneOffsetMinute < 0) {
      timezoneStandard = '+' + offsetHour + ':' + offsetMinute;
    } else if (timezoneOffsetMinute > 0) {
      timezoneStandard = '-' + offsetHour + ':' + offsetMinute;
    } else if (timezoneOffsetMinute === 0) {
      timezoneStandard = 'Z';
    }

    // console.log(postYear, postMonth, postDay, postHour, postMinute);
    // console.log(postDate);
    // console.log(timezoneStandard);

    this.publishDateTime = `${postYear}-${postMonth}-${postDay}T${postHour}:${postMinute}:00${timezoneStandard}`;
    return true;
  }

  private publishTweet() {
    this.twitterService.publishTweet(this.post.id).subscribe(
      publishedPost => {
        this.snackBar.open('Post has been published', 'Dismiss', {duration: 2000});
        console.log(publishedPost);
      }, err => {
        this.snackBar.open(`Failed to publish post`, 'Dismiss', {duration: 2000});
        console.log(err);
      }, () => {
        this.router.navigate(['/calendars', this.calendarId, 'posts']);
      }
    );
  }

  schedulePost() {
    if (this.postId) {
      this.updatePost(false, true);
    } else {
      this.createPost(false, true);
    }
  }

  publishPost() {
    if (this.postId) {
      this.updatePost(true);
    } else {
      this.createPost(true);
    }
  }
}
