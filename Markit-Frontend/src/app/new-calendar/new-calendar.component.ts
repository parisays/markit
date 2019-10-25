import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {HttpClient} from '@angular/common/http';
import {CalendarService} from '../services/calendar.service';
import {Calendar} from '@models';

@Component({
  selector: 'app-new-calendar',
  templateUrl: './new-calendar.component.html',
  styleUrls: ['./new-calendar.component.scss']
})
export class NewCalendarComponent implements OnInit {
  constructor(private service: CalendarService, private route: ActivatedRoute) {
  }

  ngOnInit() {
  }

  createCalendar(input: HTMLInputElement) {
    let calendar = {title: input.value};
    input.value = '';

    this.service.createCalendar(calendar).subscribe(
      response => {
        // calendar['id'] = response.json().id;
        console.log('new calendar has been added!');
        this.calendars.splice(0, 0, calendar);
      }
    );
  }
}
