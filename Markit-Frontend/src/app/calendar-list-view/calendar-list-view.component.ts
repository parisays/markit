import {Component, OnInit} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {AuthenticationService, CalendarService} from '@services';
import {ActivatedRoute} from '@angular/router';
import {Calendar} from '@models';

@Component({
  selector: 'app-calendar-list-view',
  templateUrl: './calendar-list-view.component.html',
  styleUrls: ['./calendar-list-view.component.scss']
})
export class CalendarListViewComponent implements OnInit {
  private calendars; // : Calendar[]
  private loading;

  constructor(private service: CalendarService, private  authService: AuthenticationService) {
  }

  ngOnInit() {
    this.loading = true;

    this.service.getAll().subscribe((response/*: any*/) => {
      console.log(response);
      this.calendars = response;
      this.loading = false;
    }, err => {
      console.log(err);
      this.loading = false;
    });
  }
}
