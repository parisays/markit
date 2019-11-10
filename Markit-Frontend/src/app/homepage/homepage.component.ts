import { Component, OnInit } from '@angular/core';
import {AuthenticationService} from '@services';

@Component({
  selector: 'app-homepage',
  templateUrl: './homepage.component.html',
  styleUrls: ['./homepage.component.scss']
})
export class HomepageComponent implements OnInit {

  constructor(private  authService: AuthenticationService) { }

  ngOnInit() {
  }

}
