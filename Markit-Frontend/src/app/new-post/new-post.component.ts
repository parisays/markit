import {Component, Input, OnInit, Output} from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {PostService} from '@services';
import {Post, PostStatus} from '@models';
import { FormGroup, FormControl, Validators} from '@angular/forms';

@Component({
  selector: 'app-new-post',
  templateUrl: './new-post.component.html',
  styleUrls: ['./new-post.component.scss']
})
export class NewPostComponent implements OnInit {
  // @Output post todo to return a new post to posts component
  /* @Input()*/ calendarId: number;
  loading = false;

  constructor(private service: PostService, private route: ActivatedRoute) { }

  form = new FormGroup({
    'title': new FormControl('', Validators.required),
    'content': new FormControl('', Validators.required)
  });

  get title()
  {
    return this.form.get('title');
  }

  get content()
  {
    return this.form.get('content');
  }

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      this.calendarId = +params.get('id');
      // service.getposts(id)
    });
  }

  createPost() {
    // let calId = this.calendarId;
    // let s=this.title
    // let post = new Post(this.title.value, this.content.value, this.calendarId);
    let post = {
      subject: this.title.value,
      text: this.content.value,
      calendar: this.calendarId,
      status: PostStatus.DRAFT
    };

    // this.title.value = '';
    // this.content.value = '';

    this.service.createPost(post).subscribe(
      response => {
        // post['id'] = response.json().id;
        console.log('new post has been added!');
        // this.posts.splice(0, 0, calendar); // todo add this new post to [post] list in posts component html
      }
    );
  }
}
