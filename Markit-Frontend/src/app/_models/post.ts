export class Post {
  id: number;
  title: string;
  content: string;
  calendarId: number;

  published ? = false;

  constructor(title: string, content: string, calendarId: number) {
    this.title = title;
    this.content = content;
    this.calendarId = calendarId;
  }
}
