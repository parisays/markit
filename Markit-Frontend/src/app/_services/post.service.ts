import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';

import {environment} from '@environments/environment';
import {Post} from '@models';
@Injectable({
  providedIn: 'root'
})
export class PostService {
  private createPostEndpoint = `${environment.apiUrl}/calendar/post/`;
  private listPostsEndpoint = `${environment.apiUrl}/calendar/post/?calendar_id=/`;

  constructor(private http: HttpClient) {
  }

  getPosts(calendarId: number) {
    return this.http.get<Post[]>(this.listPostsEndpoint + calendarId.toString());//todo give calendar id in the url
  }

  createPost(post) {
    return this.http.post(this.createPostEndpoint, JSON.stringify((post)));
  }
}
