import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders, HttpParams} from '@angular/common/http';

import {environment} from '@environments/environment';
import {Post} from '@models';
import { DataService } from './data.service';

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
    return super.getAll(new HttpParams().set('calendar_id', calendarId.toString()));
  }

}
