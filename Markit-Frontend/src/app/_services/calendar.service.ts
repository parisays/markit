import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';

import {environment} from '@environments/environment';
import {Calendar} from '@models';
import {AuthenticationService} from '@app/_services/auth.service';
import {map} from 'rxjs/operators';

@Injectable({providedIn: 'root'})
export class CalendarService {
  private calendarEndpoint = `${environment.apiUrl}/api/v1.0/calendar/`;

  constructor(private http: HttpClient, private  authService: AuthenticationService) {
  }

  getCalendars() {
    return this.http.get<Calendar[]>(this.calendarEndpoint, {
      headers: new HttpHeaders({
        Authorization: `Token ${this.authService.currentUserValue.key}`
      })
    });
  }

  createCalendar(calendar: Calendar) {
    return this.http.post<Calendar>(this.calendarEndpoint, {
      posts: [],
      user: [+this.authService.currentUserValue]
    }, {
      headers: new HttpHeaders({
        Authorization: `Token ${this.authService.currentUserValue.key}`
      })
    });
  }
}
