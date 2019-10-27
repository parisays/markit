import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';

import {environment} from '@environments/environment';
import {Calendar} from '@models';

@Injectable({providedIn: 'root'})
export class CalendarService {
  private calendarEndpoint = `${environment.apiUrl}/calendar/`;

  constructor(private http: HttpClient) {
  }

  getCalendars() {
    return this.http.get<Calendar[]>(this.calendarEndpoint);
  }

  createCalendar(calendar) {
    return this.http.post<Calendar>(this.calendarEndpoint, JSON.stringify((calendar)));
  }
}
