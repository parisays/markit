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

  ngOnInit() {
  }

  onClick() {
    this.postService.getCalendarPosts(6)
      .subscribe(value => {
        console.log(value);
      }, error => {
        console.log(error);
      });
  }
}
