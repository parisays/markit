import {Component, OnInit} from '@angular/core';
import {FormGroup, Validators, FormControl} from '@angular/forms';
import {CalendarService} from '@services';
import {ActivatedRoute} from '@angular/router';
import {Calendar} from '@models';

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

  calendarId: number;

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      this.calendarId = +params.get('calendarId');
    });

  }

  createCalendar() {
    const calendar = {
      name: this.title.value,
      collaborators: [],
      connectedPlatforms: '',
      posts: []
    } as Calendar;

    this.service.create(calendar).subscribe(
      response => {
        console.log('new calendar has been added!');
      }
    );

    this.isCreated = true;
  }

  editCalendar() {
    // this.service.get(calenarId).subscribe();
    // this.service.update();
  }
}
