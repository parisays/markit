import {Component, OnInit} from '@angular/core';
import {Calendar, Post, User} from '@models';
import {ActivatedRoute} from '@angular/router';
import {CommentService, PostService} from '@services';
import {MatSnackBar} from '@angular/material';
import {UserService} from '@app/_services/user.service';
import {Comment} from '@app/_models/comment';

@Component({
  selector: 'app-comment',
  templateUrl: './comment.component.html',
  styleUrls: ['./comment.component.scss']
})
export class CommentComponent implements OnInit {
  postId: number;
  comments: Comment[];
  loading = false;
  user: User;
  userAvatar: '../../assets/images/user-logo.png';


  submitting = false;
  inputValue = '';

  constructor(private route: ActivatedRoute,
              private commentService: CommentService,
              private userService: UserService,
              private snackBar: MatSnackBar) {
  }

  ngOnInit() {
    this.userService.getAll().subscribe((response) => {
      this.user = response as User;
      console.log(`this is user:`, this.user);
    }, err => {
      console.log(err);
    });

    this.loading = true;

    this.route.paramMap.subscribe(params => {
      this.postId = +params.get('postId');

      this.commentService.getPostComments(this.postId)
        .subscribe(commentsResponse => {
          this.comments = commentsResponse as Comment[];
          console.log('this is comments of this post', this.comments);
          this.loading = false;
        });
    }, err => {
      console.log('error while retrieving comments of a specific post', err);
      this.loading = false;
    });
  }

  createComment() {
    this.loading = true;

    const commentData = {
      post: this.postId,
      collaborator: this.user.id,
      text: this.inputValue,
    };
    console.log(`comment data:`, commentData);

    this.commentService.create(commentData).subscribe(
      (value: Comment) => {
        console.log(value);
        this.snackBar.open('Comment posted successfully!', 'Dismiss', {duration: 2000});
      }, err => {
        this.loading = false;
        this.snackBar.open('Comment creation failed!', 'Dismiss', {duration: 2000});
        console.log(err);
      }
    );
  }
}
