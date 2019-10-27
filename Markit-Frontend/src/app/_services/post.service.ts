import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';

import {environment} from '@environments/environment';
@Injectable({
  providedIn: 'root'
})
export class PostService {
  private createPostEndpoint = `${environment.apiUrl}/createPost/`;
  private listPostsEndpoint = `${environment.apiUrl}/listPosts/`;

  constructor(private http: HttpClient) {
  }

  getPosts() {
    return this.http.get(this.listPostsEndpoint);
  }

  createPost(post) {
    return this.http.post(this.createPostEndpoint, JSON.stringify((post)));
  }
}
