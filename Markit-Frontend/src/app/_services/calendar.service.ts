import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {environment} from '@environments/environment';
import {User} from '@models';

@Injectable({providedIn: 'root'})
export class CalendarService {
  private calendarEndpoint = `${environment.apiUrl}/calendars/`;


  constructor(private http: HttpClient) {
  }

  getCalendars() {
    return this.http.get(calendarEndpoint);
  }

  createCalendar(calendar) {
    return this.http.post(calendarEndpoint, JSON.stringify((calendar)));
  }
}
