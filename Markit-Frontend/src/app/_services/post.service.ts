import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders, HttpParams} from '@angular/common/http';

import {environment} from '@environments/environment';
import {Post} from '@models';
import {DataService} from './data.service';
import {catchError} from 'rxjs/operators';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PostService extends DataService {
  private readonly endpoint: string;

  // private listPostsEndpoint = `${environment.apiUrl}/calendar/post/?calendar_id=`;

  constructor(http: HttpClient) {
    const endpoint = `${environment.apiUrl}post/`;
    super(endpoint, http);
    this.endpoint = endpoint;
  }

  getCalendarPosts(calendarId: number) {
    const url = `${this.endpoint}${calendarId}`;
    return super.getAll(undefined, url);
  }

  get(id): Observable<object> {
    const url = this.endpoint + 'view/';
    return super.get(id, url);
  }

  update(resource): Observable<object> {
    const url = this.endpoint + 'edit/';
    return super.update(resource, url);
  }

  partialUpdate(id, resource): Observable<object> {
    const url = this.endpoint + 'edit/';
    return super.partialUpdate(id, resource, url);
  }

  delete(id): Observable<object> {
    const url = this.endpoint + 'delete';
    return super.delete(id, url);
  }
}
