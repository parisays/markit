import {Access} from '@app/_models/access';

export class Role {
  id: number;
  name: string;
  access: Access[];
}
