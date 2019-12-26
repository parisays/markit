export class Comment {
  id?: number;
  post: number;
  collaborator: number;
  text: string;
  reply?: string;
}
