import {Post} from '@app/_models/post';
import {User} from '@app/_models/user';

export class Calendar {
  id: number;
  name: string;
  // description?: string;
  user: number[];
  posts: Post[];

  constructor(name: string) {
    this.name = name;
  }
}
