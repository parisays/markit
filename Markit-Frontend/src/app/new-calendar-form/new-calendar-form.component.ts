import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators} from '@angular/forms';

@Component({
  selector: 'app-new-calendar-form',
  templateUrl: './new-calendar-form.component.html',
  styleUrls: ['./new-calendar-form.component.scss']
})
export class NewCalendarFormComponent implements OnInit {

  form = new FormGroup({
    'title': new FormControl('', Validators.required)
  });

  get title()
  {
    return this.form.get('title');
  }
  constructor() { }

  ngOnInit() {
  }

}
