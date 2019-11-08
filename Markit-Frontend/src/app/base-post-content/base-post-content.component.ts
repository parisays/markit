import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-base-post-content',
  templateUrl: './base-post-content.component.html',
  styleUrls: ['./base-post-content.component.scss']
})
export class BasePostContentComponent implements OnInit {

  uploadedImage: string;
  form: FormGroup = this.fb.group(
    {
      content: ['', [
        Validators.required
      ]]
    }
  );

  get content() {
    return this.form.get('content');
  }
  constructor(private fb: FormBuilder) { }

  ngOnInit() {
  }

}
