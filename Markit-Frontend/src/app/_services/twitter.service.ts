import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {environment} from '@environments/environment';
import {map, switchMap} from 'rxjs/operators';
import {throwError} from 'rxjs';
import {AuthenticationService} from '@app/_services/auth.service';

@Injectable({
  providedIn: 'root'
})
export class TwitterService {

  constructor(
    private http: HttpClient  ) {  }

  publishTweet(postId: number) {
    return this.http.get<any>(`${environment.apiUrl}twitter/tweet/${postId}`);
  }

  connect(returnUrl: string, calendarId: number) {
    return this.http.get<any>(`${environment.apiUrl}socials/twitter/oauth`).pipe(
      map(authData => {
        if (authData && authData.url) {
          localStorage.setItem('pendingCalendarTwitterConnect', calendarId.toString());
          localStorage.setItem('pendingTwitterConnectReturnUrl', returnUrl);
          return authData.url as string;
        } else {
          console.log('twitter fetch token failed');
          return throwError(new Error('twitter fetch token failed'));
        }
      }));
  }
}
