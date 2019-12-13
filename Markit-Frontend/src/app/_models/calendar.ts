import {Post} from '@app/_models/post';

export class Calendar {
  id?: number;
  name: string;
  owner?: number;
  collaborators: number[];
  posts: Post[];
  connectedPlatforms: string;
}
