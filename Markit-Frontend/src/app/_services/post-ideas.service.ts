import { Injectable } from '@angular/core';
import {DataService} from '@app/_services/data.service';
import {HttpClient} from '@angular/common/http';
import {environment} from '@environments/environment';

@Injectable({
  providedIn: 'root'
})
export class PostIdeasService extends DataService {
  private endpoint: string;

  constructor(http: HttpClient) {
    const endpoint = `${environment.apiUrl}socials/twitter/trends/`;
    super(endpoint, http);
    this.endpoint = endpoint;
  }
}
