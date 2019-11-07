import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {AuthenticationService} from '@app/_services/auth.service';
import {environment} from '@environments/environment';

@Injectable({
  providedIn: 'root'
})
export class TwitterService {

  constructor(
    private http: HttpClient,
    private authService: AuthenticationService,
  ) {  }

  publishTweet(postId: number) {
    return this.http.get<any>(`${environment.apiUrl}/api/v1.0/calendar/tweet/${postId}`, {
      headers: {
        Authorization: `Token ${this.authService.currentUserValue.key}`
      }
    });
  }
}
