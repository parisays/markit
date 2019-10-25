import {Component, OnInit} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {CalendarService} from '../services/calendar.service';

@Component({
  selector: 'app-calendars',
  templateUrl: './calendars.component.html',
  styleUrls: ['./calendars.component.scss']
})
export class CalendarsComponent implements OnInit {
  public calendars: any[]; // todo type should be calendar component

  constructor(private  service: CalendarService) {
  }

  ngOnInit() {
    this.service.getCalendars().subscribe(response => {
      // this.calendars = response.json();//todo
    });
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
