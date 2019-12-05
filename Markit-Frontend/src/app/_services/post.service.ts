import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders, HttpParams} from '@angular/common/http';

import {environment} from '@environments/environment';
import {Post} from '@models';
import {DataService} from './data.service';
import {catchError} from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class PostService extends DataService {
  private endpoint: string;

  // private listPostsEndpoint = `${environment.apiUrl}/calendar/post/?calendar_id=`;

  constructor(http: HttpClient) {
    const endpoint = `${environment.apiUrl}post/`;
    super(endpoint, http);
    this.endpoint = endpoint;
  }

  getCalendarPosts(calendarId: number) {
    // this.endpoint = this.endpoint + `${calendarId}/`;
    // console.log('endpoint in post service', this.endpoint);
    // return super.getAll();
    // return super.get(calendarId);
    // return this.http.get(this.url, { params }).pipe(
    //   catchError(this.handleError)
    // );
    let url = `${this.endpoint}${calendarId}`;
    return super.getAll(undefined, url);
  }

}
