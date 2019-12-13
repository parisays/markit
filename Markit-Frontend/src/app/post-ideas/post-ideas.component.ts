import {Component, OnInit} from '@angular/core';
import {PostIdeasService} from '@services';
import {Calendar, PostIdea} from '@models';

@Component({
  selector: 'app-post-ideas',
  templateUrl: './post-ideas.component.html',
  styleUrls: ['./post-ideas.component.scss']
})
export class PostIdeasComponent implements OnInit {
  postIdeas/*: PostIdea[] = null*/;
  loading = false;

  centered = false;
  disabled = false;
  unbounded = false;

  constructor(private service: PostIdeasService) {
  }

  ngOnInit() {
    this.loading = true;

    this.service.getAll().subscribe((response) => {
      this.postIdeas = JSON.parse(response as string);
      this.loading = false;
    }, err => {
      console.log(err);
      this.loading = false;
    });
  }


}
