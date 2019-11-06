import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-post-ideas',
  templateUrl: './post-ideas.component.html',
  styleUrls: ['./post-ideas.component.scss']
})
export class PostIdeasComponent implements OnInit {

  centered = false;
  disabled = false;
  unbounded = false;
  constructor() { }

  mockPostIdeas = [
    {
      type: 'twitter',
      lable: '#test1',
      text: 'kljckjbv;kj oskjdfoidjkjn dijfodjn ;oijf ii'
    }
  ];
  ngOnInit() {
  }

}
