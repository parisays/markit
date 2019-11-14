import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {

  firstname = 'lskdlk';
  lastname = ';lkandf';
  image = '../../assets/images/facebook-logo.png';
  email = 'sjkdfjk@lakbf.com';

  constructor() { }

  ngOnInit() {
  }

}
