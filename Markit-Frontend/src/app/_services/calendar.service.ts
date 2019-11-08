import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';

import {environment} from '@environments/environment';
import { DataService } from './data.service';

@Injectable({providedIn: 'root'})
export class CalendarService extends DataService {
  private endpoint: string;

  constructor(http: HttpClient) {
    const endpoint = `${environment.apiUrl}/calendar/`;
    super(endpoint, http);
    this.endpoint = endpoint;
  }
}
