import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';
import {FormGroup, Validators, FormControl, FormBuilder} from '@angular/forms';
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

  public form = new FormGroup({
    name: new FormControl('', Validators.required),
  });

  public imageFile: File;

  get title() {
    return this.form.controls.name;
  }

  constructor(private fb: FormBuilder) {
  }

  ngOnInit() {
  }

  onImageChanged(event) {
    this.imageFile = event.target.files[0];
  }
}
