import { Component, OnInit } from '@angular/core';
import {AuthenticationService} from '@services';
import {HttpClient, HttpHeaders} from '@angular/common/http';

import { environment } from '@environments/environment';
import {map} from 'rxjs/operators';
import {Observable, throwError} from 'rxjs';
import {Router} from '@angular/router';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {

  constructor(
    private authService: AuthenticationService,
    private http: HttpClient,
    private router: Router
  ) { }

  ngOnInit() {
  }

  // login() {
  //   this.ro
  // }

}
