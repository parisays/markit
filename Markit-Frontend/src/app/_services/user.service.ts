import {Injectable} from '@angular/core';
import {DataService} from '@app/_services/data.service';
import {HttpClient, HttpErrorResponse, HttpParams} from '@angular/common/http';
import {environment} from '@environments/environment';
import {catchError} from 'rxjs/operators';
import {throwError} from 'rxjs';
import {BadInput} from '@app/_helpers/bad-input';
import {NotFoundError} from '@app/_helpers/not-found-error';
import {AppError} from '@app/_helpers/app-error';

@Injectable({
  providedIn: 'root'
})

export class UserService extends DataService {
  private endpoint: string;

  constructor(http: HttpClient) {
    const endpoint = `${environment.apiUrl}auth/rest-auth/user/`;
    super(endpoint, http);
    this.endpoint = endpoint;
  }

  partialUpdate(resource) {
    console.log('update service is running');

    return this.http.patch(this.endpoint, resource).pipe(
      catchError(this.handleError)
    );
  }
}
