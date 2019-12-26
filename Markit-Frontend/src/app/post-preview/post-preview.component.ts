import {Component, OnInit} from '@angular/core';
import {Location} from '@angular/common';
import {ActivatedRoute, Router} from '@angular/router';
import {CalendarService, PostService, TwitterService} from '@services';
import {MatSnackBar} from '@angular/material';
import {Calendar, Post} from '@models';

@Component({
  selector: 'app-post-preview',
  templateUrl: './post-preview.component.html',
  styleUrls: ['./post-preview.component.scss']
})
export class PostPreviewComponent implements OnInit {
  calendarId: number;
  postId: number;
  post: Post = null;
  loading = false;

  constructor(private route: ActivatedRoute,
              private postService: PostService,
              private snackBar: MatSnackBar) {
  }

  ngOnInit() {
    this.loading = true;

    this.route.paramMap.subscribe(params => {
      this.postId = +params.get('postId');

      this.postService.get(this.postId)
        .subscribe(postResponse => {
          this.post = postResponse as Post;
          console.log('this is post that was retrieved', this.post);
          this.loading = false;
        });
    }, err => {
      console.log('post preview error when retrieving post', err);
      this.loading = false;
    });
  }
}
