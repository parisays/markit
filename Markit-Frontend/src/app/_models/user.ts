import {Calendar} from '@app/_models/calendar';

export class User {
  id?: number;
  firstName: string;
  lastName: string;
  email: string;
  key?: string;
  calendars?: Calendar[];
}
