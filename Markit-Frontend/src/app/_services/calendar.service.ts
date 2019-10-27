import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';

import {environment} from '@environments/environment';

@Injectable({providedIn: 'root'})
export class CalendarService {
  private calendarEndpoint = `${environment.apiUrl}/calendar/`;

  constructor(private http: HttpClient) {
  }

  getCalendars() {
    return this.http.get(this.calendarEndpoint);
  }

  createCalendar(calendar) {
    return this.http.post(this.calendarEndpoint, JSON.stringify((calendar)));
  }
}
