import {Component, OnInit} from '@angular/core';
import {FormGroup, FormBuilder, Validators} from '@angular/forms';

@Component({
  selector: 'app-base-post-content',
  templateUrl: './base-post-content.component.html',
  styleUrls: ['./base-post-content.component.scss']
})
export class BasePostContentComponent implements OnInit {

  private selectedFile: File;
  private imageUrl;
  private imageName;
  private imagePath: string;

  form: FormGroup = this.fb.group(
    {
      content: ['', [
        Validators.required
      ]]
    }
  );

  constructor(private fb: FormBuilder) {
  }

  get content() {
    return this.form.get('content');
  }

  onFileChanged(event) {
    if (event.target.files.length === 0) {
      return;
    }

    if (event.target.files[0].type.match(/image\/*/) == null) {
      console.log('Only images are supported.');
      return;
    }

    let reader = new FileReader();
    this.imagePath = event.target.files;
    reader.readAsDataURL(event.target.files[0]);
    reader.onload = (e) => {
      this.imageUrl = reader.result;
    };

    this.selectedFile = event.target.files[0];
    this.imageName = this.selectedFile.name;
  }

  ngOnInit() {
  }

}
