import {Component, OnInit, ViewChild, AfterViewInit, ChangeDetectorRef} from '@angular/core';
import {Location} from '@angular/common';
import {ActivatedRoute, Router} from '@angular/router';
import {CalendarService} from '@services';
import {Calendar} from '@models';
import {MatSnackBar, MatStepper} from '@angular/material';
import {CalendarDetailsFormComponent} from '@app/calendar-details-form/calendar-details-form.component';

@Component({
  selector: 'app-calendar-wizard',
  templateUrl: './calendar-wizard.component.html',
  styleUrls: ['./calendar-wizard.component.scss']
})
export class CalendarWizardComponent implements OnInit, AfterViewInit {
  @ViewChild('stepper', {static: false}) stepper: MatStepper;
  @ViewChild('calendar_details', {static: false}) calendarDetails: CalendarDetailsFormComponent;

  loading = false;
  calendar: Calendar = null;
  isLinear = true;
  stepComplete = [false, false, false];
  isDetailsFormValid = false;
  calendarId: number;
  access = {
    canEditCalendar: false,
  };

  get returnUrl() {
    return this.calendar ? `calendars/${this.calendar.id}/wizard/social-accounts` : null;
  }

  get closeUrl() {
    return this.calendar ? `calendars/${this.calendar.id}/posts` : `/`;
  }

  constructor(private location: Location,
              private route: ActivatedRoute,
              private router: Router,
              private service: CalendarService,
              private changeDetector: ChangeDetectorRef,
              private snackBar: MatSnackBar) {
  }

  ngOnInit(): void {
    if (this.location.isCurrentPathEqualTo(`/calendars/new`)) {
      return;
    }

    this.calendarId = +this.route.snapshot.paramMap.get('calendarId');
    if (this.calendarId) {
      this.service.getMyAccess(this.calendarId).subscribe((accObj: any) => {
          this.access.canEditCalendar = accObj.canEditCalendar;
          if (!this.access.canEditCalendar) {
            this.router.navigate(['calendars', this.calendarId, 'posts']);
          }
        }, err => {
          console.log(err);
        }
      );
    }
  }

  ngAfterViewInit() {
    if (this.calendarId) {
      this.service.getMyAccess(this.calendarId).subscribe((accObj: any) => {
          this.access.canEditCalendar = accObj.canEditCalendar;
          this.access.canEditCalendar = false;
          if (!this.access.canEditCalendar) {
            this.router.navigate(['calendars', this.calendarId, 'posts']);
          }
        }, err => {
          console.log(err);
        }
      );

      this.service.get(this.calendarId).subscribe((value: Calendar) => {
        // console.log(value);
        this.calendar = value;

        this.isLinear = false;
        this.stepComplete = [true, true, true]; // TODO bug : social-accounts route

        if (this.location.isCurrentPathEqualTo(`/calendars/${this.calendar.id}/wizard/details`)) {
          this.stepper.selectedIndex = 0;
        }
        if (this.location.isCurrentPathEqualTo(`/calendars/${this.calendar.id}/wizard/social-accounts`)) {
          this.stepper.selectedIndex = 1;
        }
        if (this.location.isCurrentPathEqualTo(`/calendars/${this.calendar.id}/wizard/collaborators`)) {
          this.stepper.selectedIndex = 2;
        }

        this.stepper.animationDone.subscribe(() => {
          if (this.stepper.selectedIndex === 0) {
            this.location.go(`/calendars/${this.calendar.id}/wizard/details`);
          }
          if (this.stepper.selectedIndex === 1) {
            this.location.go(`/calendars/${this.calendar.id}/wizard/social-accounts`);
          }
          if (this.stepper.selectedIndex === 2) {
            this.location.go(`/calendars/${this.calendar.id}/wizard/collaborators`);
          }
        });

        this.calendarDetails.form.controls.name.setValue(this.calendar.name);
      }, err => {
        console.log(err);
        this.router.navigate(['calendars', 'new']);
      });
    }

    this.calendarDetails.form.valueChanges.subscribe(() => this.isDetailsFormValid = this.calendarDetails.form.valid);

    this.changeDetector.detectChanges();
  }

  createCalendar() {
    this.loading = true;
    const cf = this.calendarDetails.form.controls;
    this.service.create({name: cf.name.value}).subscribe(
      (value: Calendar) => {
        // console.log(value);
        this.snackBar.open('Calendar created successfully!', 'Dismiss', {duration: 2000});
        this.router.navigate(['calendars', value.id, 'wizard']);
      }, err => {
        this.loading = false;
        this.snackBar.open('Calendar creation failed!', 'Dismiss', {duration: 2000});
        console.log(err);
      }
    );
  }

  updateCalendar() {
    this.loading = true;
    const updatedCalendar: Calendar = this.calendar;
    updatedCalendar.name = this.calendarDetails.form.controls.name.value;
    this.service.partialUpdate(updatedCalendar.id, {name: updatedCalendar.name})
      .subscribe((value: Calendar) => {
          // console.log(value);
          this.snackBar.open('Calendar updated successfully!', 'Dismiss', {duration: 1000});
          this.loading = false;
        }, err => {
          this.loading = false;
          this.snackBar.open('Calendar updating failed!', 'Dismiss', {duration: 1000});
          console.log(err);
        }
      );
  }

  finish() {
    this.updateCalendar();
    this.router.navigate(['calendars', this.calendar.id, 'posts']);
  }
}

