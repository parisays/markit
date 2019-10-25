import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators} from '@angular/forms';

@Component({
  selector: 'app-new-twitter-post-form',
  templateUrl: './new-twitter-post-form.component.html',
  styleUrls: ['./new-twitter-post-form.component.scss']
})
export class NewTwitterPostFormComponent implements OnInit {

  form = new FormGroup({
    'title': new FormControl('', Validators.required),
    'content': new FormControl('', Validators.required)
  });

  get title()
  {
    return this.form.get('title');
  }
  
  get content()
  {
    return this.form.get('content');
  }
  constructor() { }

  ngOnInit() {
  }

}
