import { BadInput } from '../_helpers/bad-input';
import { NotFoundError } from '../_helpers/not-found-error';
import { AppError } from '../_helpers/app-error';
import { Injectable } from '@angular/core';
import {HttpClient, HttpErrorResponse, HttpResponse} from '@angular/common/http';
import {throwError} from 'rxjs';
import {catchError, map} from 'rxjs/operators';

@Injectable()
export class DataService {
  constructor(private url: string, private http: HttpClient) { }

  getAll() {
    return this.http.get(this.url).pipe(
      catchError(this.handleError)
    );
  }

  create(resource) {
    return this.http.post(this.url, resource).pipe(
      catchError(this.handleError)
    );
  }

  update(resource) {
    return this.http.put(this.url + '/' + resource.id, resource).pipe(
      catchError(this.handleError)
    );
  }

  partialUpdate(resource) {
    return this.http.patch(this.url + '/' + resource.id, resource).pipe(
      catchError(this.handleError)
    );
  }

  delete(id) {
    return this.http.delete(this.url + '/' + id).pipe(
      catchError(this.handleError)
    );
  }

  private handleError(error: HttpErrorResponse) {
    if (error.status === 400) {
      return throwError(new BadInput(error));
    }

    if (error.status === 404) {
      return throwError(new NotFoundError());
    }

    return throwError(new AppError(error));
  }
}
