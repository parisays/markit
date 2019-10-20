import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators} from '@angular/forms'

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  form = new FormGroup({
    'email': new FormControl('', [
      Validators.email,
      Validators.required
    ]),
    password: new FormControl('', Validators.required)
});

get email(){
  return this.form.get('email');
}

get password(){
  return this.form.get('password')
}

hide = true;

constructor() { }

ngOnInit() {
}

}
