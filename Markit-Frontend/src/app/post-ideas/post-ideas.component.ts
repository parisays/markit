import {Component, OnInit} from '@angular/core';
import {PostIdeasService} from '@services';
import {Calendar, PostIdea} from '@models';

@Component({
  selector: 'app-post-ideas',
  templateUrl: './post-ideas.component.html',
  styleUrls: ['./post-ideas.component.scss']
})
export class PostIdeasComponent implements OnInit {
  private postIdeas/*: PostIdea[] = null*/;
  private loading = false;

  centered = false;
  disabled = false;
  unbounded = false;

  constructor(private service: PostIdeasService) {
  }

  ngOnInit() {
    // this.loading = true;
    //
    // this.service.getAll().subscribe((response: PostIdea[]) => {
    //   console.log(response);
    //   this.postIdeas = response;
    //   this.loading = false;
    // }, err => {
    //   console.log(err);
    //   this.loading = false;
    // });

    this.postIdeas = [
      {
        type: 'twitter',
        label: '#Flashback\n',
        text: 'Post an image of the early days of your brand, or even funnier, of the founder of your brand as a child!'
      },
      {
        type: ' pinterest',
        label: '#FeelGoodDay',
        text: 'Post feel-good images or quotes related to your brand, industry or domain of expertise.'
      },
      {
        type: 'facebook',
        label: 'Quote',
        text: 'Everybody loves a good word: delight your audience with an inspiring or funny quote, expression or idiom.'
      },
      {
        type: 'twitter',
        label: 'Miami Beach Pop Festival',
        text: 'Miami Beach Pop Festival is proud to debut one of the most diverse, cross-genre, and collaborative music festival lineups in the world'
      },
      {
        type: 'pinterest',
        label: 'National S.T.E.M Day\n',
        text: 'Full S.T.E.A.M. ahead! November 8 is a day meant to inspire kids to explore and pursue their interests in Science, Technology, Engineering, Art and Math. '
      }
    ];
  }


}
