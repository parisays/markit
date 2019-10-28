import { Component, Input, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { PostService } from '@services';
import { ActivatedRoute } from '@angular/router';
import { Post } from '@models';
import { animate, state, style, transition, trigger } from '@angular/animations';

@Component({
  selector: 'app-posts',
  templateUrl: './posts.component.html',
  styleUrls: ['./posts.component.scss'],
  animations: [
    trigger('detailExpand', [
      state('collapsed', style({ height: '0px', minHeight: '0' })),
      state('expanded', style({ height: '*' })),
      transition('expanded <=> collapsed', animate('225ms cubic-bezier(0.4, 0.0, 0.2, 1)')),
    ]),
  ],
})
export class PostsComponent implements OnInit {
  /*@Input()*/
  isTwitterConnected = true;

  dataSource: Post[]; //data source is posts // public posts: Post[];
  // dataSource = this.ELEMENT_DATA;
  columnsToDisplay = ['title'];
  expandedElement: Post | null;

  calendarId: number;


  constructor(private service: PostService, private route: ActivatedRoute) {
    this.dataSource = this.ELEMENT_DATA;
  }

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      this.calendarId = +params.get('id');
      this.service.getPosts(this.calendarId).subscribe(response => {
        // this.dataSource = response.json();//todo get lists
      });
    });
  }


  ELEMENT_DATA: Post[] = [
    {
      id: 1,
      calendar: 11,
      name: 'Hydrogen',
      text: `Hydrogen is a chemical element with symbol H and atomic number 1. With a standard
        atomic weight of 1.008, hydrogen is the lightest element on the periodic table.`
    }, {
      id: 2,
      calendar: 11,
      name: 'Helium',
      text: `Helium is a chemical element with symbol He and atomic number 2. It is a
        colorless, odorless, tasteless, non-toxic, inert, monatomic gas, the first in the noble gas
        group in the periodic table. Its boiling point is the lowest among all the elements.`
    }, {
      id: 3,
      calendar: 11,
      name: 'Lithium',
      text: `Lithium is a chemical element with symbol Li and atomic number 3. It is a soft,
        silvery-white alkali metal. Under standard conditions, it is the lightest metal and the
        lightest solid element.`
    },
  ];

}
