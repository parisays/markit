import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-post-status',
  templateUrl: './post-status.component.html',
  styleUrls: ['./post-status.component.scss']
})
export class PostStatusComponent implements OnInit {

  data = {
    Draft : 1,
    Scheduled : 5,
    Published : 0
  };

  constructor() { }

  ngOnInit() {
  }

}
