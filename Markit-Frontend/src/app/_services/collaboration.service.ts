import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {DataService} from '@app/_services/data.service';
import {environment} from '@environments/environment';

@Injectable({
  providedIn: 'root'
})
export class CollaborationService extends DataService {
  private readonly endpoint: string;

  constructor(http: HttpClient) {
    const endpoint = `${environment.apiUrl}collaboration/`;
    super(endpoint, http);
    this.endpoint = endpoint;
  }

  activate(token: string) {
    const u = `${this.endpoint}activate/${token}`;
    return this.create({}, u);
  }
}
