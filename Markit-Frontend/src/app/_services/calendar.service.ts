import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';

import {environment} from '@environments/environment';

@Injectable({providedIn: 'root'})
export class CalendarService {
  private createCalendarEndpoint = `${environment.apiUrl}/createCalendar/`;
  private listCalendarsEndpoint = `${environment.apiUrl}/listCalendars/`;

  constructor(private http: HttpClient) {
  }

  getCalendars() {
    return this.http.get(this.listCalendarsEndpoint);
  }

  createCalendar(calendar) {
    return this.http.post(this.createCalendarEndpoint, JSON.stringify((calendar)));
  }
}
