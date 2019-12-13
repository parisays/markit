import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-forget-pass',
  templateUrl: './forget-pass.component.html',
  styleUrls: ['./forget-pass.component.scss']
})
export class ForgetPassComponent implements OnInit {

  form: FormGroup = this.fb.group({
    email: ['', [
      Validators.email,
      Validators.required
    ]]
  });

  get email() {
    return this.form.get('email');
  }
  constructor(private fb: FormBuilder) { }

  ngOnInit() {
  }

}
