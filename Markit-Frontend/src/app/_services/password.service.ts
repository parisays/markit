import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {environment} from '@environments/environment';
import {DataService} from '@app/_services/data.service';

@Injectable({
  providedIn: 'root'
})
export class PasswordService extends DataService {
  private endpoint: string;

  constructor(http: HttpClient) {
    const endpoint = `${environment.apiUrl}auth/rest-auth/password/`;
    super(endpoint, http);
    this.endpoint = endpoint;
  }

  requestPasswordReset(resource) {
    const url = this.endpoint + 'reset/';
    return super.create(resource, url);
  }

  confirmPasswordReset(resource) {
    const url = this.endpoint + 'reset/confirm/';
    return super.create(resource, url);
  }
}
