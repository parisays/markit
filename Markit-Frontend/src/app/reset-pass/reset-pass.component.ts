import { Component, OnInit } from '@angular/core';
import { FormGroup, Validators, FormBuilder } from '@angular/forms';

@Component({
  selector: 'app-reset-pass',
  templateUrl: './reset-pass.component.html',
  styleUrls: ['./reset-pass.component.scss']
})
export class ResetPassComponent implements OnInit {

  form: FormGroup = this.fb.group({
    password: ['', [
      Validators.required
    ]],
    confirm: ['', [
      Validators.required
    ]]
  });

  hide = true;

  get password() {
    return this.form.get('password');
  }

  get confirm() {
    return this.form.get('confirm');
  }
  constructor(private fb: FormBuilder) { }

  ngOnInit() {
  }

}
