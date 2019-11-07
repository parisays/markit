import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder } from '@angular/forms';
import { Subject } from 'rxjs';

@Component({
  selector: 'app-post-details-form',
  templateUrl: './post-details-form.component.html',
  styleUrls: ['./post-details-form.component.scss']
})
export class PostDetailsFormComponent implements OnInit {

  form: FormGroup = this.fb.group({
      subject: [''],
      date: ['']
    }
  );

  tempDate = new Date(Date.now());
  constructor(
    private fb: FormBuilder
    ) {
    }

  ngOnInit() {
  }

}
