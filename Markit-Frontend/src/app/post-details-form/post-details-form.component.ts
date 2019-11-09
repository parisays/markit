import {Component, OnInit} from '@angular/core';
import {FormGroup, FormBuilder} from '@angular/forms';
import {Subject} from 'rxjs';

@Component({
  selector: 'app-post-details-form',
  templateUrl: './post-details-form.component.html',
  styleUrls: ['./post-details-form.component.scss']
})
export class PostDetailsFormComponent implements OnInit {

  private postSubject;
  private postDate;

  form: FormGroup = this.fb.group({
      subject: [''],
      date: ['']
    }
  );

  tempDate = new Date(Date.now());

  constructor(private fb: FormBuilder) {
  }

  get subject() {
    return this.form.get('subject');
  }

  get date() {
    return this.form.get('date');
  }

  ngOnInit() {
  }

}
