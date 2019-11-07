import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {HttpClient} from '@angular/common/http';
import {CalendarService} from '@services';
import {Calendar} from '@models';
import { FormGroup, FormControl, Validators} from '@angular/forms';

@Component({
  selector: 'app-new-calendar',
  templateUrl: './new-calendar.component.html',
  styleUrls: ['./new-calendar.component.scss']
})
export class NewCalendarComponent implements OnInit {
  loading = false;


  form = new FormGroup({
    'title': new FormControl('', Validators.required)
  });

  get title()
  {
    return this.form.get('title');
  }

  constructor(private service: CalendarService, private route: ActivatedRoute) {
  }

  ngOnInit() {
  }

  createCalendar() {
    // let calendar = new Calendar (this.title.value);
    const calendar = {
      name: this.title.value,
      collaborators: [],
      connectedPlatforms: '',
      posts: []
    } as Calendar;
    // input.value = '';

    this.service.createCalendar(calendar).subscribe(
      response => {
        // calendar['id'] = response.json().id;
        console.log('new calendar has been added!');
        // this.calendars.splice(0, 0, calendar); // todo add this new calendar to calendars list in calendars component html
      }
    );
  }
}
