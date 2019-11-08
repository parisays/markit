import { Component, OnInit } from '@angular/core';
import {CalendarService, PostService} from '@services';

@Component({
  selector: 'app-manual-test',
  templateUrl: './manual-test.component.html',
  styleUrls: ['./manual-test.component.scss']
})
export class ManualTestComponent implements OnInit {

  constructor(private calendarService: CalendarService,
              private postService: PostService) { }

  private selectedFile: File;

  ngOnInit() {
  }

  onFileChanged(event) {
    this.selectedFile = event.target.files[0];
  }

  onUpload() {
    const uploadData = new FormData();
    uploadData.append('calendar', '2');
    uploadData.append('image', this.selectedFile, this.selectedFile.name);
    uploadData.append('subject', 'with img');
    uploadData.append('text', 'test_text');
    this.postService.create(uploadData).subscribe(
      value => {
        console.log(value);
      }, err => {
        console.log(err);
      }
    );
  }
}
