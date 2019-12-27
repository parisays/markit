import {Access, Post} from '@app/_models/';
import {Collaborator} from '@app/_models/';

export class Calendar {
  id?: number;
  name: string;
  owner?: number;
  // tslint:disable-next-line:variable-name
  collaborator_calendar: Collaborator[];
  posts: Post[];
  connectedPlatforms: string;
  role: string;
  access?: Access[];
}
