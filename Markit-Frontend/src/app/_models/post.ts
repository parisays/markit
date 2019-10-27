export class Post {
  id: number;
  title: string;
  content: string;
  calendarId: number;

  constructor(title: string, content: string, calendarId: number) {
    this.title = title;
    this.content = content;
    this.calendarId = calendarId;
  }
}
