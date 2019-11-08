import {Component, Input, OnInit} from '@angular/core';
import {CalendarService, TwitterService} from '@services';
import {ActivatedRoute} from '@angular/router';
import {Post, PostStatus} from '@models';
import {map} from 'rxjs/operators';
import {throwError} from 'rxjs';

@Component({
  selector: 'app-social-accounts-connection',
  templateUrl: './social-accounts-connection.component.html',
  styleUrls: ['./social-accounts-connection.component.scss']
})
export class SocialAccountsConnectionComponent implements OnInit {
<<<<<<< HEAD
  @Input() calendarId: number;
  @Input() returnURL: string;

=======
  private calendarId: number;
  private calendar;
>>>>>>> Frontend/dev
  socialAccounts = [
    {
      image: '../assets/images/twitter-logo.png',
      name: 'Twitter',
      connect: this.connectTwitter,
    },
    {
      image: '../assets/images/facebook-logo.png',
      name: 'Facebook',
      connect: this.connectFB,
    },
    {
      image: '../assets/images/pinterest-logo.png',
      name: 'Pinterest',
      connect: this.connectPinterest,
    }
  ];

  constructor(private route: ActivatedRoute,
              private twitter: TwitterService) {
  }

  ngOnInit() {
    console.log(this.calendarId, this.returnURL);
  }

  private connectTwitter(c: SocialAccountsConnectionComponent) {
    console.log(c.calendarId);
    console.log(c.returnURL);
    if (!c.calendarId || !c.returnURL) { return; }
    console.log('b');

    c.twitter.connect(c.returnURL as string, c.calendarId as number)
      .subscribe(twitterUrl => {
        console.log(twitterUrl);
        window.location.href = twitterUrl as string;
      }, error => {
        console.log('twitter routing failed');
        console.log(error);
      });
  }

  private connectFB(c: SocialAccountsConnectionComponent) { }

  private connectPinterest(c: SocialAccountsConnectionComponent) { }

}
