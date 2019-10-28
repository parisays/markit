export class Post {
  id: number;
  name: string;
  text: string;
  calendar: number;

  published ? = false;

  constructor(title: string, content: string, calendarId: number) {
    this.name = title;
    this.text = content;
    this.calendar = calendarId;
  }
}
