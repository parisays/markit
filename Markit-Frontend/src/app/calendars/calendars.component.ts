import {Component, OnInit} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {AuthenticationService, CalendarService} from '@services';
import {ActivatedRoute} from '@angular/router';
import {Calendar} from '@models';

@Component({
  selector: 'app-calendars',
  templateUrl: './calendars.component.html',
  styleUrls: ['./calendars.component.scss']
})
export class CalendarsComponent implements OnInit {
  calendars: Calendar[];
  loading = false;

  constructor(private service: CalendarService, private  authService: AuthenticationService) {
  }

  ngOnInit() {
    console.log('calendars component running');
    this.service.getCalendars().subscribe((response: Calendar[]) => {
      console.log(response);
      this.calendars = response;
      // = response.json();//todo
    });
  }
}
