import {Component, OnInit} from '@angular/core';
import {FormBuilder, Validators, FormGroup} from '@angular/forms';
import {PasswordService} from '@services';

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

  constructor(private fb: FormBuilder, private service: PasswordService) {
  }

  get email() {
    return this.form.get('email');
  }

  ngOnInit() {
  }

  onSubmit() {
    this.service.requestPasswordReset(this.email);
  }
}
