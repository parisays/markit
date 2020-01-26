import {Role} from '@app/_models/role';

export class Collaborator {
  id: number;
  user: number;
  calendar: number;
  role: Role;
  firstName: string;
  lastName: string;
  email: string;
}
