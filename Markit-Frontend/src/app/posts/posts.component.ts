import {Component, Input, OnInit} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {PostService} from '@services';
import {ActivatedRoute} from '@angular/router';
import {Post} from '@models';

@Component({
  selector: 'app-posts',
  templateUrl: './posts.component.html',
  styleUrls: ['./posts.component.scss']
})
export class PostsComponent implements OnInit {
  /*@Input()*/
  calendarId: number;

  public posts: Post[];

  constructor(private service: PostService, private route: ActivatedRoute) {
  }

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      this.calendarId = +params.get('id');
      this.service.getPosts(this.calendarId).subscribe(response => {
        // this.calendars = response.json();//todo get lists
      });
    });
  }

}
