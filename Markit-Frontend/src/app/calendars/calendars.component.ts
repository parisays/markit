import {Component, OnInit} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {CalendarService} from '@services';
import {ActivatedRoute} from '@angular/router';
import {Calendar} from '@models';

@Component({
  selector: 'app-calendars',
  templateUrl: './calendars.component.html',
  styleUrls: ['./calendars.component.scss']
})
export class CalendarsComponent implements OnInit {
  public calendars: Calendar[];

  constructor(private service: CalendarService) {
  }

  ngOnInit() {
    this.service.getCalendars().subscribe(response => {
      // this.calendars = response.json();//todo
    });
  }
}
