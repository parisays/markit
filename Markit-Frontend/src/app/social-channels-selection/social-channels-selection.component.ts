import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-social-channels-selection',
  templateUrl: './social-channels-selection.component.html',
  styleUrls: ['./social-channels-selection.component.scss']
})
export class SocialChannelsSelectionComponent implements OnInit {

  isTwitterSelected = false;
  isPinterestSelected = false;
  isFacebookSelected = false;

  connectedPlatforms: string[] = [];

  get twitterEnabled() {
    return this.isTwitterSelected && this.connectedPlatforms.includes('Twitter');
  }
  constructor() { }

  ngOnInit() {
  }

}
