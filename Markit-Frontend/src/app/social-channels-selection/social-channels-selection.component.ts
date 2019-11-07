import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-social-channels-selection',
  templateUrl: './social-channels-selection.component.html',
  styleUrls: ['./social-channels-selection.component.scss']
})
export class SocialChannelsSelectionComponent implements OnInit {

  isTwitterSelected = false;
  isPinterstSelected = false;
  isFacebookSelected = false;
  constructor() { }

  ngOnInit() {
  }

}
