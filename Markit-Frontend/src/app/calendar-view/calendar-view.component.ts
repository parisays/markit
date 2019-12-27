import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-calendar-view',
  templateUrl: './calendar-view.component.html',
  styleUrls: ['./calendar-view.component.scss']
})
export class CalendarViewComponent implements OnInit {

  posts = [
    {
      title: 'test1',
      date: new Date(Date.now())
    },
    {
      title: 'test2',
      date: new Date('2019-12-25T03:00:00Z')
    },
    {
      title: 'test3test3test3test3test3',
      date: new Date('2019-12-24T03:00:00Z')
    },
    {
      title: 'test4',
      date: new Date('2019-12-24T03:00:00Z')
    },
    {
      title: 'test5',
      date: new Date('2019-12-25T04:30:00Z')
    },
    {
      title: 'test6',
      date: new Date('2019-12-25T04:30:00Z')
    },
    {
      title: 'test7',
      date: new Date('2019-12-25T04:30:00Z')
    },
    {
      title: 'test8',
      date: new Date('2019-12-25T04:30:00Z')
    },
  ];

  isInTrueDate(date1: Date, date2: Date): boolean {
    return date1.getDate() === date2.getDate()
        && date1.getMonth() === date2.getMonth()
        && date1.getFullYear() === date2.getFullYear();
  }
  constructor() { }

  ngOnInit() {
  }

}
