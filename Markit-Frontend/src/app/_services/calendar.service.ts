import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';

import {environment} from '@environments/environment';
import {Calendar} from '@models';

@Injectable({providedIn: 'root'})
export class CalendarService {
  private calendarEndpoint = `${environment.apiUrl}/api/v1.0/calendar/`;

  constructor(private http: HttpClient) {
  }

  getCalendars() {
    return this.http.get<any>(this.calendarEndpoint);
  }

  createCalendar(calendar: Calendar) {
    return this.http.post<Calendar>(this.calendarEndpoint, {
      posts: []
    });
  }
}
