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
  private twitterAppData: { client_id: string, secret: string };

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
}
