import {Component, EventEmitter, OnInit, Output, ViewChild} from '@angular/core';
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
export class CalendarWizardComponent implements OnInit {
  @ViewChild('stepper', { static: false }) stepper : MatStepper;

  constructor(private location: Location,
              private route: ActivatedRoute,
              private router: Router,
              private service: CalendarService) {
  }

  calendarId: number;
  calendar/*: Calendar*/;
  // @Output() animationDone: EventEmitter<void>;

  ngOnInit() {
    // this.stepper.animationDone.subscribe(() => {
    //   if (this.stepper.selectedIndex === 0) {
    //     this.location.go(`/calendars/${this.calendarId}/wizard/details`);
    //   }
    //   if (this.stepper.selectedIndex === 1) {
    //     this.location.go(`/calendars/${this.calendarId}/wizard/social-accounts`);
    //   }
    // });

    this.route.paramMap.subscribe(params => {
      this.calendarId = +params.get('calendarId');
    });

    console.log(this.calendarId);

    if (this.calendarId) { // edit existing calendar
      this.route.url.subscribe((value) => {
        console.log(this.router.url);
        if (this.router.url === `/calendars/${this.calendarId}/wizard/details`) {
          this.stepper.selectedIndex = 0;
        }
        if (this.router.url === `/calendars/${this.calendarId}/wizard/social-accounts`) {
          this.stepper.selectedIndex = 1;
        }
      });
    }
    // else {// create new calendar
    //   this.stepper.selectedIndex = 0;
    // } todo check if necessary

  }

  stepperSelectionChange() {// todo
    
  }
}
