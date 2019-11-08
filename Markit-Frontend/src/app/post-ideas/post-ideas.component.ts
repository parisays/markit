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
    },
    {
      type: 'pinterest',
      lable: '#test2',
      text: 'kljckjbv;kj oskjdfoidjkjn dijfodjn ;oijf ii'
    },
    {
      type: 'facebook',
      lable: '#test3',
      text: 'kljckjbv;kj oskjdfoidjkjn dijfodjn ;oijf ii'
    },
    {
      type: 'twitter',
      lable: '#test1',
      text: 'kljckjbv;kj oskjdfoidjkjn dijfodjn ;oijf ii'
    },
    {
      type: 'pinterest',
      lable: '#test2',
      text: 'kljckjbv;kj oskjdfoidjkjn dijfodjn ;oijf ii'
    },
    {
      type: 'facebook',
      lable: '#test3',
      text: 'kljckjbv;kj oskjdfoidjkjn dijfodjn ;oijf ii'
    }
  ];
  ngOnInit() {
  }

}
