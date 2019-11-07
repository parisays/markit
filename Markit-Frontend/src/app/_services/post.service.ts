import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';

import {environment} from '@environments/environment';
import {Post} from '@models';

@Injectable({
  providedIn: 'root'
})
export class PostService {
  private createPostEndpoint = `${environment.apiUrl}/api/v1.0/calendar/post/`;
  private listPostsEndpoint = `${environment.apiUrl}/api/v1.0/calendar/post/?calendar_id=`;

  constructor(private http: HttpClient) {
  }

  getPosts(calendarId: number) {
    return this.http.get<Post[]>(this.listPostsEndpoint + calendarId.toString());
  }

  createPost(post) {
    return this.http.post(this.createPostEndpoint, post);
  }
}
