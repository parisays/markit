import {Component, OnInit, Output} from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {HttpClient} from '@angular/common/http';
import {PostService} from '@services';
import {Post} from '@models';

@Component({
  selector: 'app-new-post',
  templateUrl: './new-post.component.html',
  styleUrls: ['./new-post.component.scss']
})
export class NewPostComponent implements OnInit {
  // @Output post todo to return a new post to posts component
  constructor(private service: PostService, private route: ActivatedRoute) { }

  ngOnInit() {
  }

  createPost(input: HTMLInputElement) {
    let post = {title: input.value};
    input.value = '';

    this.service.createPost(post).subscribe(
      response => {
        // post['id'] = response.json().id;
        console.log('new post has been added!');
        // this.posts.splice(0, 0, calendar); // todo add this new post to [post] list in posts component html
      }
    );
  }
}
