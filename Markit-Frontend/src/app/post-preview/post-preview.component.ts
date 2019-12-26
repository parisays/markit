import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-post-preview',
  templateUrl: './post-preview.component.html',
  styleUrls: ['./post-preview.component.scss']
})
export class PostPreviewComponent implements OnInit {

  post = {
    name: 'test',
    text: 'We supply a series of design principles, practical patterns and high quality design resources' +
    '(Sketch and Axure), to help people create their product prototypes beautifully and efficiently.',
    image: '../../assets/images/sample-3.jpg',
    date: new Date(Date.now()),
  };

  constructor() { }

  ngOnInit() {
  }

}
