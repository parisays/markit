import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-social-accounts-connection',
  templateUrl: './social-accounts-connection.component.html',
  styleUrls: ['./social-accounts-connection.component.scss']
})
export class SocialAccountsConnectionComponent implements OnInit {


  socialAccounts = [
    {
      image: '../assets/images/twitter-logo.png',
      name: 'Twitter'
    },
    {
      image: '../assets/images/facebook-logo.png',
      name: 'Facebook'
    },
    {
      image: '../assets/images/pinterest-logo.png',
      name: 'Pinterest'
    }
  ];

  constructor() { }

  ngOnInit() {
  }

}
