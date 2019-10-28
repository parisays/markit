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

    this.http.get<any>(`${environment.apiUrl}/api/v1.0/auth/twitter/verify/${oauthToken}/${oauthVerifier}/`, {
      headers: {
        Authorization: `Token ${this.authService.currentUserValue.key}`
      }
    }).pipe(
      map((data: { access_token: string, token_secret: string }) => {
        if (!data) {
          return throwError(new Error('access token fetching failed'));
        } else {
          return data;
        }
      })
    ).subscribe((data: { access_token: string, token_secret: string }) => {
      console.log(data);
      this.http.post<any>(`${environment.apiUrl}/api/v1.0/auth/rest-auth/twitter/connect/`, data, {
          headers: {
            Authorization: `Token ${this.authService.currentUserValue.key}`
          }
        }
      ).subscribe(d => {
          console.log('twitter connected!!');
          localStorage.setItem('twitterLinked', 'true');
        },
       e => {
        console.log('twitter connection failed!');
      }, () => {
        this.router.navigate(['/']);
      });
    }, er => {
      console.log('ERROR');
      console.log(er);
    });
  }

}
