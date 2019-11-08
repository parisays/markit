import {Component, EventEmitter, OnInit, Output, ViewChild, AfterViewInit, ChangeDetectorRef} from '@angular/core';
import {Location} from '@angular/common';
import {ActivatedRoute, Router} from '@angular/router';
import {CalendarService} from '@services';
import {Calendar} from '@models';
import { MatStepper } from '@angular/material';

@Component({
  selector: 'app-calendar-wizard',
  templateUrl: './calendar-wizard.component.html',
  styleUrls: ['./calendar-wizard.component.scss']
})
export class CalendarWizardComponent implements AfterViewInit {
  @ViewChild('stepper', { static: false }) stepper: MatStepper;

  constructor(private location: Location,
              private route: ActivatedRoute,
              private service: CalendarService,
              private changeDetector: ChangeDetectorRef) {
    }

    calendarId: number;
    calendar/*: Calendar*/;
    // @Output() animationDone: EventEmitter<void>;

  ngAfterViewInit() {
    this.stepperSelectionChange();

    this.route.paramMap.subscribe(params => {
      this.calendarId = +params.get('calendarId');
    });

    console.log(this.calendarId);

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

  stepperSelectionChange() {// todo
    this.stepper.animationDone.subscribe(() => {
      if (this.stepper.selectedIndex === 0) {
        this.location.go(`/calendars/${this.calendarId}/wizard/details`);
      }
      if (this.stepper.selectedIndex === 1) {
        this.location.go(`/calendars/${this.calendarId}/wizard/social-accounts`);
      }
    });
  }
}
