import {Component, OnInit} from '@angular/core';
import {ActivatedRoute, Router} from '@angular/router';
import {throwError} from 'rxjs';
import {map} from 'rxjs/operators';
import {HttpClient} from '@angular/common/http';

import {environment} from '@environments/environment';
import {AuthenticationService} from '@services';
import {error} from 'util';

@Component({
  selector: 'app-twitter-auth',
  templateUrl: './twitter-auth.component.html',
  styleUrls: ['./twitter-auth.component.scss']
})
export class TwitterAuthComponent implements OnInit {
  private accessToken: string;
  private tokenSecret: string;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private http: HttpClient,
    private authService: AuthenticationService
  ) {
  }

  ngOnInit() {
    const oauthToken = this.route.snapshot.queryParamMap.get('oauth_token');
    const oauthVerifier = this.route.snapshot.queryParamMap.get('oauth_verifier');

    const calendarId = localStorage.getItem('pendingCalendarTwitterConnect');

    this.http.get<any>(`${environment.apiUrl}socials/twitter/connect/${oauthToken}/${oauthVerifier}/${calendarId}`).pipe(
      map((data: { access_token: string, token_secret: string }) => {
        if (!data) {
          return throwError(new Error('access token fetching failed'));
        } else {
          return data;
        }
      })
    ).subscribe((data) => {
      console.log(data);
      const returnUrl = localStorage.getItem('pendingTwitterConnectReturnUrl');
      this.router.navigate(returnUrl.split('/'));
    }, er => {
      console.log('ERROR');
      console.log(er);
    }, () => {
      localStorage.removeItem('pendingCalendarTwitterConnect');
      localStorage.removeItem('pendingTwitterConnectReturnUrl');
    });
  }

}
