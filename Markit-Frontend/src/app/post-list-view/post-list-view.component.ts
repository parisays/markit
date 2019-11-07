import { Component, Input, OnInit } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {AuthenticationService, PostService} from '@services';
import {ActivatedRoute, Router} from '@angular/router';
import {Post, PostStatus, Calendar} from '@models';
import { animate, state, style, transition, trigger } from '@angular/animations';
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
      state('collapsed', style({ height: '0px', minHeight: '0' })),
      state('expanded', style({ height: '*' })),
      transition('expanded <=> collapsed', animate('225ms cubic-bezier(0.4, 0.0, 0.2, 1)')),
    ]),
  ],
})
export class PostListViewComponent implements OnInit {
  private twitterAppData: { client_id: string, secret: string };

  constructor(private service: PostService,
              private route: ActivatedRoute,
              private twitter: TwitterService,
              private snackBar: MatSnackBar,
              private authService: AuthenticationService,
              private http: HttpClient,
              private router: Router) {
    this.dataSource = this.ELEMENT_DATA;
    this.calendars = [
      {
        id: 12,
        name: 'skdjhfjk',
        connectedPlatforms: 'dlkfn',
        posts: this.dataSource,
        collaborators: [1]
      },
      {
        id: 22,
        name: 'jhfjk',
        connectedPlatforms: 'dlkfn',
        posts: this.dataSource,
        collaborators: [1]
      }
    ];
    this.selectedCalendar = {
      id: 12,
      name: 'skdjhfjk',
      connectedPlatforms: 'dlkfn',
      posts: this.dataSource,
      collaborators: [1]
    };
  }
  /*@Input()*/
  get isTwitterConnected() {
    const twitterLinkedStorage = localStorage.getItem('twitterLinked');
    if (twitterLinkedStorage) {
      return twitterLinkedStorage === 'true';
    } else { return false; }
  }

  calendars: Calendar[]; // calendars to show in select menu
  selectedCalendar: Calendar;

  dataSource: Post[]; // data source is posts // public posts: Post[];
  // dataSource = this.ELEMENT_DATA;
  columnsToDisplay = ['connected-platforms', 'subject', 'status'];
  expandedElement: Post | null;

  calendarId: number;

  ELEMENT_DATA: Post[] = [
    {
      id: 1,
      calendar: 11,
      subject: 'Hydrogen',
      text: `Hydrogen is a chemical element with symbol H and atomic number 1. With a standard
        atomic weight of 1.008, hydrogen is the lightest element on the periodic table.`,
      status: 'draft'
    }, {
      id: 2,
      calendar: 11,
      subject: 'Helium',
      text: `Helium is a chemical element with symbol He and atomic number 2. It is a
        colorless, odorless, tasteless, non-toxic, inert, monatomic gas, the first in the noble gas
        group in the periodic table. Its boiling point is the lowest among all the elements.`,
      status: 'draft'
    }, {
      id: 3,
      calendar: 11,
      subject: 'Lithium',
      text: `Lithium is a chemical element with symbol Li and atomic number 3. It is a soft,
        silvery-white alkali metal. Under standard conditions, it is the lightest metal and the
        lightest solid element.`,
      status: 'published'
    },
  ];

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      this.calendarId = +params.get('id');
      this.service.getCalendarPosts(this.calendarId)
      .subscribe(response => {
        console.log(response);
        this.dataSource = response as Post[]; // todo get lists
        console.log(this.dataSource);
      });
    });
  }

  onTwitterAuth() {
    this.http.get<any>(`${environment.apiUrl}/api/v1.0/auth/twitter/`, {
      headers: new HttpHeaders({
        Authorization: `Token ${this.authService.currentUserValue.key}`
      })
    }).pipe(
      map(data => {
        if (data && data.provider && data.provider === 'twitter') {
          return {
            client_id: data.client_id as string,
            secret: data.secret as string
          };
        } else {
          return throwError(new Error('twitter oauth failed'));
        }
      })
    ).subscribe(data => {
        this.twitterAppData = data as { client_id: string, secret: string };
        console.log(data);
        this.http.get<any>(`${environment.apiUrl}/api/v1.0/auth/twitter/oauth`, {
          headers: {
            Authorization: `Token ${this.authService.currentUserValue.key}`
          }
        }).pipe(map(authData => {
          if (authData && authData.url) {
            return authData.url as string;
          } else {
            return throwError(new Error('twitter fetch token failed'));
          }
        })).subscribe(twitterUrl => {
          console.log(twitterUrl);
          window.location.href = twitterUrl as string;
        }, error => {
          console.log('twitter routing failed');
        });
      },
      error => {
        console.log(error);
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
