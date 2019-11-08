import { Component, OnInit } from '@angular/core';
import {FormGroup, Validators, FormBuilder} from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { AuthenticationService } from '@services';
import { first } from 'rxjs/operators';
import {MatSnackBar} from '@angular/material';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  loginForm: FormGroup = this.fb.group({
    email: ['', [
      Validators.email,
      Validators.required
    ]],
    password: ['', Validators.required]
  });
  loading = false; // TODO clean up
  submitted = false;
  returnUrl: string;
  error = '';

  hide = true;

  constructor(
    private fb: FormBuilder,
    private route: ActivatedRoute,
    private router: Router,
    private authService: AuthenticationService,
    private snackBar: MatSnackBar,
  ) {
    if (this.authService.currentUserValue) {
      this.router.navigate(['/']);
    }
  }

  get f() { return this.loginForm.controls; }

  ngOnInit() {
    this.returnUrl = this.route.snapshot.queryParams.returnUrl || '/';
  }

  onSubmit() {
    this.submitted = true;

    if (this.loginForm.invalid) {
      return;
    }

    this.loading = true;
    this.authService.login(this.f.email.value, this.f.password.value)
      .pipe(
        first()
      ).subscribe(
        data => {
          this.router.navigate([this.returnUrl]);
        },
        err => {
          this.error = err;
          this.loading = false;
          this.snackBar.open('Login failed!', 'Dismiss', { duration: 5000 });
        }
      );
  }
}
