import { Component, OnInit } from '@angular/core';
import {animate, state, style, transition, trigger} from '@angular/animations';

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

  dataSource = ELEMENT_DATA;
  columnsToDisplay = ['title', 'date', 'time'];
  expandedElement: Post | null;
  constructor() { }

  ngOnInit() {
  }

}

export interface Post {
  title: string;
  date: string;
  time: string;
  content: string;
}

const ELEMENT_DATA: Post[] = [
  {
    title: 'Hydrogen',
    time: '12:23:24',
    date: '1/9/1999',
    content: `Hydrogen is a chemical element with symbol H and atomic number 1. With a standard
        atomic weight of 1.008, hydrogen is the lightest element on the periodic table.`
  }, {
    title: 'Helium',
    time: '2:3:32',
    date: '2/4/1987',
    content: `Helium is a chemical element with symbol He and atomic number 2. It is a
        colorless, odorless, tasteless, non-toxic, inert, monatomic gas, the first in the noble gas
        group in the periodic table. Its boiling point is the lowest among all the elements.`
  }, {
    title: 'Lithium',
    time: '12:23:24',
    date: '12/23/2009',
    content: `Lithium is a chemical element with symbol Li and atomic number 3. It is a soft,
        silvery-white alkali metal. Under standard conditions, it is the lightest metal and the
        lightest solid element.`
  },
];
