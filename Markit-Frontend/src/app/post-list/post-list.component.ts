import { Component, OnInit } from '@angular/core';
import {animate, state, style, transition, trigger} from '@angular/animations';
import { PostService } from '@services';
import { Post } from '@models';

@Component({
  selector: 'app-post-list',
  templateUrl: './post-list.component.html',
  styleUrls: ['./post-list.component.scss'],
  animations: [
    trigger('detailExpand', [
      state('collapsed', style({height: '0px', minHeight: '0'})),
      state('expanded', style({height: '*'})),
      transition('expanded <=> collapsed', animate('225ms cubic-bezier(0.4, 0.0, 0.2, 1)')),
    ]),
  ],
})
export class PostListComponent implements OnInit {

  isTwitterConnected = false;

  dataSource = ELEMENT_DATA; //data source is posts
  columnsToDisplay = ['title'];
  expandedElement: Post | null;
  constructor(private service: PostService) { }

  ngOnInit() {
    this.service.getPosts().subscribe(response => {
      // this.calendars = response.json();//todo
    });
  }

}

const ELEMENT_DATA: Post[] = [
  {
    title: 'Hydrogen',
    content: `Hydrogen is a chemical element with symbol H and atomic number 1. With a standard
        atomic weight of 1.008, hydrogen is the lightest element on the periodic table.`
  }, {
    title: 'Helium',
    content: `Helium is a chemical element with symbol He and atomic number 2. It is a
        colorless, odorless, tasteless, non-toxic, inert, monatomic gas, the first in the noble gas
        group in the periodic table. Its boiling point is the lowest among all the elements.`
  }, {
    title: 'Lithium',
    content: `Lithium is a chemical element with symbol Li and atomic number 3. It is a soft,
        silvery-white alkali metal. Under standard conditions, it is the lightest metal and the
        lightest solid element.`
  },
];
