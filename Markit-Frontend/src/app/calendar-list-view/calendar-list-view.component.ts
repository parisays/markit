import {Component, OnInit} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {AuthenticationService, CalendarService} from '@services';
import {ActivatedRoute} from '@angular/router';
import {Calendar} from '@models';

@Component({
  selector: 'app-calendar-list-view',
  templateUrl: './calendar-list-view.component.html',
  styleUrls: ['./calendar-list-view.component.scss']
})
export class CalendarListViewComponent implements OnInit {
  calendars: Calendar[];
  loading = false;

  constructor(private service: CalendarService, private  authService: AuthenticationService) {
  }

  ngOnInit() {
    console.log('calendars component running');
    this.service.getAll().subscribe((response: any) => {
      console.log(response);
      this.calendars = response;
      // = response.json();//todo
    }, err => {
      console.log(err);
    });
  }
}
