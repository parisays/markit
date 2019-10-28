import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';

import {environment} from '@environments/environment';
import {Post} from '@models';
import {AuthenticationService} from '@app/_services/auth.service';

@Injectable({
  providedIn: 'root'
})
export class PostService {
  private createPostEndpoint = `${environment.apiUrl}/api/v1.0/calendar/post/`;
  private listPostsEndpoint = `${environment.apiUrl}/api/v1.0/calendar/post/?calendar_id=`;

  constructor(private http: HttpClient, private  authService: AuthenticationService) {
  }

  getPosts(calendarId: number) {
    return this.http.get<Post[]>(this.listPostsEndpoint + calendarId.toString(), {
      headers: new HttpHeaders({
        Authorization: `Token ${this.authService.currentUserValue.key}`
      })
    });// todo give calendar id in the url
  }

  createPost(post) {
    return this.http.post(this.createPostEndpoint, JSON.stringify((post)), {
      headers: new HttpHeaders({
        Authorization: `Token ${this.authService.currentUserValue.key}`
      })
    });
  }
}
