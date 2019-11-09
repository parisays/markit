import {Component, OnInit} from '@angular/core';
import {CalendarService, PostService} from '@services';
import {Calendar} from '@models';

@Component({
  selector: 'app-manual-test',
  templateUrl: './manual-test.component.html',
  styleUrls: ['./manual-test.component.scss']
})
export class ManualTestComponent implements OnInit {

  constructor(private calendarService: CalendarService,
              private postService: PostService) {
  }

  private selectedFile: File;

  ngOnInit() {
  }

  onFileChanged(event) {
    this.selectedFile = event.target.files[0];
  }

  onUpload() {
    const uploadData = new FormData();
    uploadData.append('calendar', '3');
    uploadData.append('image', this.selectedFile, this.selectedFile.name);
    uploadData.append('subject', 'with img sajdfjklas');
    uploadData.append('text', 'test_text');

    this.postService.create(uploadData).subscribe(
      value => {
        console.log(value);
      }, err => {
        console.log(err);
      }
    );

    this.postService.getCalendarPosts(3)
      .subscribe(value => {
        console.log('get calendar result: ', value);
      }, error => {
        console.log(error);
      });
  }

  onClick() {
    let calendar = {
      name: 'calendar Name 1234',
    };

    this.calendarService.create(calendar).subscribe(response => {
      console.log('create calendar response: ', response);
    }, error => {
      console.log(error);
    });

    console.log('start of testing');
    let post = {
      calendar: 10,
      subject: 'post subject 123',
      text: 'post text 123',
    };

    this.postService.create(post).subscribe(response => {
      console.log('create post response: ', response);
    }, error => {
      console.log('errorrrrrrrrrrrrrr: ', error);
    });

    this.postService.getCalendarPosts(9)
      .subscribe(value => {
        console.log('get calendar result: ', value);
      }, error => {
        console.log(error);
      });
  }
  
  onClick() {
    // let calendar = {
    //   name: 'calendar Name 1234',
    // };
    //
    // this.calendarService.create(calendar).subscribe(response => {
    //   this.newCalendar = response;
    //   console.log('create calendar response: ', response);
    // }, error => {
    //   console.log(error);
    // });

    console.log('start of testing');
    let post = {
      calendar: 10,
      subject: 'post subject 123',
      text: 'post text 123',
    };

    this.postService.create(post).subscribe(response => {
      console.log('create post response: ', response);
    }, error => {
      console.log('errorrrrrrrrrrrrrr: ', error);
    });

    // this.postService.getCalendarPosts(this.newCalendar.id)
    //   .subscribe(value => {
    //     console.log('get calendar result: ', value);
    //   }, error => {
    //     console.log(error);
    //   });
  }
}
