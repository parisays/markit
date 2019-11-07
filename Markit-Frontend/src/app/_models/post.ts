export class Post {
  id?: number;
  subject: string;
  text: string;
  calendar: number;
  status: string;
}

export enum PostStatus {
  PUBLISHED = 'Published',
  DRAFT = 'Draft'
}
