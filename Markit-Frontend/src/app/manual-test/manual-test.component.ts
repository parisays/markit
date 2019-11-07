import { Component, OnInit } from '@angular/core';
import {CalendarService} from '@services';

@Component({
  selector: 'app-manual-test',
  templateUrl: './manual-test.component.html',
  styleUrls: ['./manual-test.component.scss']
})
export class ManualTestComponent implements OnInit {

  constructor(private calendarService: CalendarService) { }

  ngOnInit() {
  }

  onClick() {
    this.calendarService.getAll()
      .subscribe(value => {
        console.log(value);
      }, error => {
        console.log(error);
      });
  }
}
