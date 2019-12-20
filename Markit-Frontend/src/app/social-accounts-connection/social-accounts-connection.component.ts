import {Component, Input, OnInit} from '@angular/core';
import {CalendarService, TwitterService} from '@services';
import {Calendar} from '@models';


@Component({
  selector: 'app-social-accounts-connection',
  templateUrl: './social-accounts-connection.component.html',
  styleUrls: ['./social-accounts-connection.component.scss']
})
export class SocialAccountsConnectionComponent implements OnInit {
  @Input() calendarId: number;
  @Input() returnURL: string;

  socialAccounts = [
    {
      image: '../assets/images/twitter-logo.png',
      name: 'Twitter',
      connect: this.connectTwitter,
      connected: false,
    },
    {
      image: '../assets/images/facebook-logo.png',
      name: 'Facebook',
      connect: this.connectFB,
      connected: false,
    },
    {
      image: '../assets/images/pinterest-logo.png',
      name: 'Pinterest',
      connect: this.connectPinterest,
      connected: false
    }
  ];

  constructor(private twitter: TwitterService,
              private calendarService: CalendarService) {
  }

  ngOnInit() {
    console.log(this.calendarId, this.returnURL);
    this.calendarService.get(this.calendarId).subscribe((res: Calendar) => {
        this.socialAccounts[0].connected = res.connectedPlatforms.split(',').includes('Twitter');
        this.socialAccounts[1].connected = res.connectedPlatforms.split(',').includes('Facebook');
        this.socialAccounts[2].connected = res.connectedPlatforms.split(',').includes('Pinterest');
    });
  }

  private connectTwitter(c: SocialAccountsConnectionComponent) {
    if (!c.calendarId || !c.returnURL) { return; }

    c.twitter.connect(c.returnURL as string, c.calendarId as number)
      .subscribe(twitterUrl => {
        window.location.href = twitterUrl as string;
      }, error => {
        console.log('twitter routing failed');
        console.log(error);
      });
  }

  private connectFB() { }

  private connectPinterest() { }

}
