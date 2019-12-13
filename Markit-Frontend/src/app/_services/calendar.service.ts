import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';

import {environment} from '@environments/environment';
import { DataService } from './data.service';
import {Observable} from 'rxjs';

@Injectable({providedIn: 'root'})
export class CalendarService extends DataService {
  private readonly endpoint: string;

  constructor(http: HttpClient) {
    const endpoint = `${environment.apiUrl}calendar/`;
    super(endpoint, http);
    this.endpoint = endpoint;
  }

  get(id): Observable<object> {
    const url = this.endpoint + 'view/';
    return super.get(id, url);
  }

  update(resource): Observable<object> {
    const url = this.endpoint + 'edit/';
    return super.update(resource, url);
  }

  partialUpdate(id, resource): Observable<object> {
    const url = this.endpoint + 'edit/';
    return super.partialUpdate(id, resource, url);
  }

  delete(id): Observable<object> {
    const url = this.endpoint + 'delete';
    return super.delete(id, url);
  }
}
