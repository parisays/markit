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
    return this.http.get<any>(`${environment.apiUrl}calendar/tweet/${postId}`);
  }

  isConnected(): boolean {
    const twitterLinkedStorage = localStorage.getItem('twitterLinked');
    return !!twitterLinkedStorage && (twitterLinkedStorage === 'true');
  }

  connect() {
    return this.http.get<any>(`${environment.apiUrl}auth/twitter/`).pipe(
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
    ).pipe(switchMap(data => {
        console.log(data);
        return this.http.get<any>(`${environment.apiUrl}auth/twitter/oauth`).pipe(
          map(authData => {
            if (authData && authData.url) {
              return authData.url as string;
            } else {
              return throwError(new Error('twitter fetch token failed'));
            }
          }));
      }));
  }
}
