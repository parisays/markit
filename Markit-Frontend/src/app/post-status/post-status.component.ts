import { Component, OnInit } from '@angular/core';
import { PostService } from '@services';
import { PostsStatusCount } from '@models';

@Component({
  selector: 'app-post-status',
  templateUrl: './post-status.component.html',
  styleUrls: ['./post-status.component.scss']
})
export class PostStatusComponent implements OnInit {

  loading = false;
  data: PostsStatusCount = {Draft: 0, Published: 0, Scheduled: 0};

  constructor(private service: PostService) { }

  ngOnInit() {
    this.loading = true;

    this.service.getPostsStatusCount().subscribe((response/*: any*/) => {
      // console.log(response);
      this.data = response as PostsStatusCount;
      this.loading = false;
    }, err => {
      console.log('post status view error');
      console.log(err);
      this.loading = false;
    });
  }

}
