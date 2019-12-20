import {Component, OnInit} from '@angular/core';
import {FormBuilder, Validators, FormGroup} from '@angular/forms';
import {PasswordService} from '@services';
import {MatSnackBar} from '@angular/material';
import {Router} from '@angular/router';

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

  constructor(private fb: FormBuilder,
              private service: PasswordService,
              private snackBar: MatSnackBar,
              private router: Router) {
  }

  get email() {
    return this.form.get('email').value;
  }

  ngOnInit() {
  }

  onSubmit() {
    console.log(`email is:`, this.email);
    this.service.requestPasswordReset({email: this.email}).subscribe(v => {
      this.snackBar.open('Please Check your email!', 'OK', {duration: 3000});
      this.router.navigate(['/']);
    }, err => {
      console.log(err);
    });
  }
}
