import { Component, OnInit } from '@angular/core';
import { FormGroup, Validators, FormControl } from '@angular/forms';
import { CalendarService } from '@services';
import { ActivatedRoute } from '@angular/router';
import { Calendar } from '@models';

@Component({
  selector: 'app-calendar-details-form',
  templateUrl: './calendar-details-form.component.html',
  styleUrls: ['./calendar-details-form.component.scss']
})
export class CalendarDetailsFormComponent implements OnInit {
  loading = false;
  isCreated = false;

  form = new FormGroup({
    title: new FormControl('', Validators.required)
  });

  get title() {
    return this.form.get('title');
  }

  constructor(private service: CalendarService, private route: ActivatedRoute) {
  }

  ngOnInit() {
  }

  createCalendar() {
    // let calendar = new Calendar (this.title.value);
    let calendar: Calendar = {
      name: this.title.value,
      collaborators: [],
      connectedPlatforms: '',
      posts: []
    };
    // input.value = '';

    this.service.create(calendar).subscribe(
      response => {
        // calendar['id'] = response.json().id;
        console.log('new calendar has been added!');
        // this.calendars.splice(0, 0, calendar); // todo add this new calendar to calendars list in calendars component html
      }
    );
  }
}
