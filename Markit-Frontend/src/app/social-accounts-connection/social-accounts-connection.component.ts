import {Component, OnInit} from '@angular/core';
import {CalendarService} from '@services';
import {ActivatedRoute} from '@angular/router';

@Component({
  selector: 'app-social-accounts-connection',
  templateUrl: './social-accounts-connection.component.html',
  styleUrls: ['./social-accounts-connection.component.scss']
})
export class SocialAccountsConnectionComponent implements OnInit {
  private calendarId: number;
  private calendar;
  socialAccounts = [
    {
      image: '../assets/images/twitter-logo.png',
      name: 'Twitter',
      authLink: 'twitter-auth'
    },
    {
      image: '../assets/images/facebook-logo.png',
      name: 'Facebook',
      authLink: 'facebook-auth'
    },
    {
      image: '../assets/images/pinterest-logo.png',
      name: 'Pinterest',
      authLink: 'pinterest-auth'
    }
  ];

  constructor(private route: ActivatedRoute) {
  }

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      this.calendarId = +params.get('calendarId');
    });
  }

}
