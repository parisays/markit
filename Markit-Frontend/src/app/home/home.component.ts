import { Component, OnInit } from '@angular/core';
import {AuthenticationService} from '@services';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  constructor(
    private authService: AuthenticationService
  ) { }

  ngOnInit() {
  }

  // login() {
  //   this.ro
  // }
}
