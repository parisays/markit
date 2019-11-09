import {Component, Input, OnInit} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {AuthenticationService, CalendarService, PostService} from '@services';
import {ActivatedRoute, Router} from '@angular/router';
import {Post, PostStatus, Calendar} from '@models';
import {animate, state, style, transition, trigger} from '@angular/animations';
import {TwitterService} from '@services';
import {map} from 'rxjs/operators';
import {throwError} from 'rxjs';
import {MatSnackBar} from '@angular/material';
import {environment} from '@environments/environment';

@Component({
  selector: 'app-post-list-view',
  templateUrl: './post-list-view.component.html',
  styleUrls: ['./post-list-view.component.scss'],
  animations: [
    trigger('detailExpand', [
      state('collapsed', style({height: '0px', minHeight: '0'})),
      state('expanded', style({height: '*'})),
      transition('expanded <=> collapsed', animate('225ms cubic-bezier(0.4, 0.0, 0.2, 1)')),
    ]),
  ],
})

export class PostListViewComponent implements OnInit {

  private calendars; // : Calendar[]
  private calendarId: number;
  private loading = false;
  returnUrl = `calendars/${this.calendarId}/posts`;
  selectedCalendar: Calendar;
  dataSource: Post[]; // data source is posts
  columnsToDisplay = ['subject', 'connected-platforms', 'status'];
  expandedElement: Post | null;

  private twitterAppData: { client_id: string, secret: string };

  constructor(private postService: PostService,
              private calendarService: CalendarService,
              private route: ActivatedRoute,
              private twitter: TwitterService,
              private snackBar: MatSnackBar) {
  }

  get isTwitterConnected() {
    return true;

    // todo uncomment
    // const twitterLinkedStorage = localStorage.getItem('twitterLinked');
    // if (twitterLinkedStorage) {
    //   return twitterLinkedStorage === 'true';
    // } else {
    //   return false;
    // }
  }

  ngOnInit() {
    this.loading = true;

    this.route.paramMap.subscribe(params => {
      this.calendarId = +params.get('calendarId');
      console.log(this.calendarId);

      this.postService.getCalendarPosts(this.calendarId)
        .subscribe(response => {
          // console.log(response);
          this.dataSource = response as Post[];
          // console.log(`posts of this calendar ${this.calendarId}: `, this.dataSource);
          this.loading = false;
        });
    }, err => {
      console.log(err);
      this.loading = false;
    });

    this.calendarService.getAll().subscribe((response/*: any*/) => {
      // console.log(response);
      this.calendars = response;
    }, err => {
      console.log(err);
    });
  }


  publishOnTweeter(post: Post) {
    console.log(post);
    this.twitter.publishTweet(post.id)
      .pipe(map(
        (res: string) => {
          if (res === 'true') {
            return 1;
          }
          return throwError('twitter failed to publish');
        }
      )).subscribe(res => {
        console.log(`twitter published ${res}`);
        post.status = PostStatus.PUBLISHED;
        // post.published = true;
      }, error => {
        console.log(error);
        this.snackBar.open('Failed to publish the post on twitter', 'Dismiss', {
          duration: 3000
        });
      }
    );
  }
}
