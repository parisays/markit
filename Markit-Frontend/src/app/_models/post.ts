export class Post {
  id?: number;
  subject: string;
  text: string;
  calendar: number;
  status: string;
  image?: string;
}

export enum PostStatus {
  PUBLISHED = 'Published',
  DRAFT = 'Draft'
}
