export class Post {
  id: number;
  name: string;
  text: string;
  calendar: number;

  constructor(name: string, text: string, calendar: number) {
    this.name = name;
    this.text = text;
    this.calendar = calendar;
  }
}
