import {Component, EventEmitter, OnInit, Output, ViewChild, AfterViewInit, ChangeDetectorRef} from '@angular/core';
import {Location} from '@angular/common';
import {ActivatedRoute, Router} from '@angular/router';
import {CalendarService} from '@services';
import {Calendar} from '@models';
import {MatSnackBar, MatStepper} from '@angular/material';

@Component({
  selector: 'app-calendar-wizard',
  templateUrl: './calendar-wizard.component.html',
  styleUrls: ['./calendar-wizard.component.scss']
})
export class CalendarWizardComponent implements AfterViewInit {
  @ViewChild('stepper', {static: false}) stepper: MatStepper;

  private loading = false;
  private isCreated = false;
  calendarId: number;
  calendar/*: Calendar*/;

  constructor(private location: Location,
              private route: ActivatedRoute,
              private router: Router,
              private service: CalendarService,
              private changeDetector: ChangeDetectorRef,
              private snackBar: MatSnackBar) {
  }

  ngAfterViewInit() {
    this.stepperSelectionChange();

    this.route.paramMap.subscribe(params => {
      this.calendarId = +params.get('calendarId');
    });

    if (this.calendarId || this.calendarId === 0) {
      this.service.get(this.calendarId).subscribe(response => {
          this.calendar = response;
          this.isCreated = true;
        }
      );
    }

    if (this.calendarId || this.calendarId === 0) { // edit existing calendar
      this.route.url.subscribe((value) => {
        console.log(value);
        if (this.location.isCurrentPathEqualTo(`/calendars/${this.calendarId}/wizard/details`)) {
          this.stepper.selectedIndex = 0;
        }
        if (this.location.isCurrentPathEqualTo(`/calendars/${this.calendarId}/wizard/social-accounts`)) {
          this.stepper.selectedIndex = 1;
        }
      });
    }
    // else {// create new calendar
    //   this.stepper.selectedIndex = 0;
    // } todo check if necessary

    this.changeDetector.detectChanges();
  }

  stepperSelectionChange() {
    this.stepper.animationDone.subscribe(() => {
      if (this.stepper.selectedIndex === 0) {
        this.location.go(`/calendars/${this.calendarId}/wizard/details`);
      }
      if (this.stepper.selectedIndex === 1) {
        this.location.go(`/calendars/${this.calendarId}/wizard/social-accounts`);
      }
    });
  }

  createCalendar() {
    this.loading = true;

    const calendar = {
      name: this.title.value,
      collaborators: [],
      connectedPlatforms: '',
      posts: []
    } as Calendar;

    this.service.create(calendar).subscribe(
      response => {
        console.log('new calendar has been added!');
        console.log(response);

        this.calendar = response;
        this.router.navigate(['calendars', this.calendarId, 'wizard/social-accounts']);
        this.isCreated = true;
      }, err => {
        console.log(err);
        this.snackBar.open('Calendar Creation Failed!', 'OK');
        // this.loading = false;
      }
    );

    this.loading = false;
  }

  editCalendar() {
    if (this.calendarId) {
      this.service.get(this.calendarId).subscribe(response => {
          this.calendar = response;
        },
        err => {
          console.log(err);
          this.snackBar.open('Calendar Creation Failed!', 'OK');
        }
      );

      this.calendar.name = this.title.value; // todo check if not ok declare as a calendar

      this.service.update(this.calendar).subscribe((response) => {
          this.calendar = response;
        },
        err => {
          console.log(err);
          this.snackBar.open('Calendar Edition Failed!', 'OK');
        });
    }
  }


}
