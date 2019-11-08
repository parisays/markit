import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';
import {FormGroup, Validators, FormControl} from '@angular/forms';
import {CalendarService} from '@services';
import {ActivatedRoute, Router} from '@angular/router';
import {Calendar} from '@models';
import {MatSnackBar} from '@angular/material';

@Component({
  selector: 'app-calendar-details-form',
  templateUrl: './calendar-details-form.component.html',
  styleUrls: ['./calendar-details-form.component.scss']
})
export class CalendarDetailsFormComponent implements OnInit {
  @Input() inputTitle: string;
  @Output() outputTitle = new EventEmitter();

  form = new FormGroup({
    title: new FormControl('', Validators.required)
  });

  // private loading = false;
  // private isCreated = false;
  // private calendarId: number;
  // private calendar/*: Calendar*/;

  // private error: '';

  get title() {
    return this.form.get('title');
  }

  constructor(/*private service: CalendarService,
              private route: ActivatedRoute,
              private router: Router,
              private snackBar: MatSnackBar*/) {
  }

  ngOnInit() {
  }

  // this.route.paramMap.subscribe(params => {
  //   this.calendarId = +params.get('calendarId');
  // });
  //
  // if (this.calendarId) {
  //   this.service.get(this.calendarId).subscribe(response => {
  //       this.calendar = response;
  //       this.isCreated = true;
  //     }
  //   );
  // }


  // createCalendar() {
  //   this.loading = true;
  //
  //   const calendar = {
  //     name: this.title.value,
  //     collaborators: [],
  //     connectedPlatforms: '',
  //     posts: []
  //   } as Calendar;
  //
  //   this.service.create(calendar).subscribe(
  //     response => {
  //       console.log('new calendar has been added!');
  //       console.log(response);
  //
  //       this.calendar = response;
  //       this.router.navigate(['calendars', this.calendarId, 'wizard/social-accounts']);
  //       this.isCreated = true;
  //     }, err => {
  //       console.log(err);
  //       this.snackBar.open('Calendar Creation Failed!', 'OK');
  //       // this.loading = false;
  //     }
  //   );
  //
  //   this.loading = false;
  // }
  //
  // editCalendar() {
  //   if (this.calendarId) {
  //     this.service.get(this.calendarId).subscribe(response => {
  //         this.calendar = response;
  //       },
  //       err => {
  //         console.log(err);
  //         this.snackBar.open('Calendar Creation Failed!', 'OK');
  //       }
  //     );
  //
  //     this.calendar.name = this.title.value; // todo check or declare as a calendar
  //
  //     this.service.update(this.calendar).subscribe((response) => {
  //         this.calendar = response;
  //       },
  //       err => {
  //         console.log(err);
  //         this.snackBar.open('Calendar Edition Failed!', 'OK');
  //       });
  //   }
  // }
}
