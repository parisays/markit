import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {environment} from '@environments/environment';
import {DataService} from './data.service';
import {Observable} from 'rxjs';

@Injectable({providedIn: 'root'})
export class CommentService extends DataService {
  private readonly endpoint: string;

  constructor(http: HttpClient) {
    const endpoint = `${environment.apiUrl}comment/`;
    super(endpoint, http);
    this.endpoint = endpoint;
  }

  getPostComments(postId: number) {
    const url = `${this.endpoint}${postId}`;
    return super.getAll(undefined, url);
  }
}
