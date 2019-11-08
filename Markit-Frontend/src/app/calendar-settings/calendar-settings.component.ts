import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';

@Component({
  selector: 'app-calendar-settings',
  templateUrl: './calendar-settings.component.html',
  styleUrls: ['./calendar-settings.component.scss']
})
export class CalendarSettingsComponent implements OnInit {

  form = new FormGroup({
    title: new FormControl('', Validators.required)
  });

  get title() {
    return this.form.get('title');
  }

  constructor() { }

  ngOnInit() {
  }

}
