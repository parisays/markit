import { Component, OnInit } from '@angular/core';
import {FormGroup, Validators, FormBuilder, ValidationErrors, AbstractControl, FormControl} from '@angular/forms';
import {ActivatedRoute, Router} from '@angular/router';
import {AuthenticationService} from '@services';
import {first, last, map, tap} from 'rxjs/operators';
import {MatSnackBar} from '@angular/material';
import {concat, forkJoin} from 'rxjs';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.scss']
})
export class SignupComponent implements OnInit {

  constructor(
    private fb: FormBuilder,
    private route: ActivatedRoute,
    private router: Router,
    private authService: AuthenticationService,
    private snackBar: MatSnackBar
  ) {
    if (this.authService.currentUserValue) {
      this.router.navigate(['/']);
    }
  }

  get f() { return this.signupForm.controls; }
  signupForm: FormGroup = this.fb.group({
    firstName: ['', Validators.required],
    lastName: ['', Validators.required],
    email: ['', [
      Validators.required,
      Validators.email
    ]],
    password: ['', Validators.required],
    confirmPassword: ['', [Validators.required, SignupComponent.matchValues('password')] ]
  });
  private returnUrl: string;
  private error: '';
  private reqLoading = false;

  hide = true;

  public static matchValues(
    matchTo: string // name of the control to match to
  ): (AbstractControl) => ValidationErrors | null {
    return (control: AbstractControl): ValidationErrors | null => {
      return !!control.parent &&
      !!control.parent.value &&
      control.value === control.parent.controls[matchTo].value
        ? null
        : { isMatching: false };
    };
  }

  ngOnInit() {
    this.returnUrl = this.route.snapshot.queryParams.returnUrl || '/';
  }

  onSubmit() {
    this.reqLoading = true;

    const formData: any = {
      email: this.f.email.value,
      password: this.f.password.value,
      firstName: this.f.firstName.value,
      lastName: this.f.lastName.value
    };

    concat(this.authService.register(formData.email, formData.password, formData.firstName, formData.lastName))
      .subscribe(
      data => {
        this.snackBar.open('Registration successful!', 'Dismiss', { duration: 3000 });
        this.router.navigate([this.returnUrl]);
      },
      err => {
        console.log(err);
        this.error = err;
        let errMsg = 'Registration failed!';
        if (err.error) {
          errMsg = [].concat(...Object.values(err.error))[0];
        }
        this.snackBar.open(errMsg, 'Dismiss');
        this.reqLoading = false;
      }
    );
  }
}
