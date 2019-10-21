import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators} from '@angular/forms'
@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.scss']
})
export class SignupComponent implements OnInit {

  form = new FormGroup({
    name: new FormControl('', Validators.required),
    'lastName': new FormControl('', Validators.required),
    'email': new FormControl('', [
      Validators.required,
      Validators.email
    ]),
    password: new FormControl('', Validators.required),
    'confirmPassword': new FormControl('', Validators.required)//add validation to match password
  });

  get name(){
    return this.form.get('name');
  }
  get lastName(){
    return this.form.get('lastName');
  }
  get email(){
    return this.form.get('email');
  }
  get password(){
    return this.form.get('password');
  }
  get confirmPassword(){
    return this.form.get('confirmPassword')
  }

  hide = true;

  constructor() { }

  ngOnInit() {
  }

}
