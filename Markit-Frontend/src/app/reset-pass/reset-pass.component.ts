import {Component, OnInit} from '@angular/core';
import {FormGroup, Validators, FormBuilder} from '@angular/forms';
import {PasswordService} from '@services';
import {MatSnackBar} from '@angular/material';
import {ActivatedRoute, Router} from '@angular/router';

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
  token;
  uid;

  constructor(private fb: FormBuilder,
              private service: PasswordService,
              private snackBar: MatSnackBar,
              private router: Router,
              private route: ActivatedRoute) {
  }

  get password() {
    return this.form.get('password');
  }

  get confirm() {
    return this.form.get('confirm');
  }

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      this.token = +params.get('uid');
      this.uid = +params.get('token');

    });
  }

  onSubmit() {
    if (this.password !== this.confirm) {
      this.snackBar.open('Passwords should match!!', 'OK', {duration: 2000});
      return;
    }

    const passReset = {
      new_password1: this.password,
      new_password2: this.confirm,
      uid: this.uid,
      token: this.token
    };

    this.service.confirmPasswordReset(passReset).subscribe(response => {
      console.log(response);
      this.snackBar.open('You can now use your new password!', 'OK', {duration: 3000});
      this.router.navigate(['/login']);
    }, err => {
      console.log(err);
    });
  }

}
