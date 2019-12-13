import {BadInput} from '../_helpers/bad-input';
import {NotFoundError} from '../_helpers/not-found-error';
import {AppError} from '../_helpers/app-error';
import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse, HttpParams} from '@angular/common/http';
import {throwError} from 'rxjs';
import {catchError, map} from 'rxjs/operators';
import {Data} from '@angular/router';

export abstract class DataService {
  constructor(private url: string, protected http: HttpClient) {
  }

  getAll(params?: HttpParams, url?: string) {
    const u = url ? url : this.url;
    return this.http.get(u, { params }).pipe(
      catchError(this.handleError)
    );
  }

  get(id, url?: string) {
    const u = url ? url : this.url;
    return this.http.get(`${u}${id.toString()}/`).pipe(
      catchError(this.handleError)
    );
  }

  create(resource, url?: string) {
    const u = url ? url : this.url;
    return this.http.post(u, resource).pipe(
      catchError(this.handleError)
    );
  }

  update(resource, url?: string) {
    const u = url ? url : this.url;
    return this.http.put(u + resource.id + '/', resource).pipe(
      catchError(this.handleError)
    );
  }

  partialUpdate(id, resource, url?: string) {
    const u = url ? url : this.url;
    return this.http.patch(u + id.toString() + '/', resource).pipe(
      catchError(this.handleError)
    );
  }

  delete(id, url?: string) {
    const u = url ? url : this.url;
    return this.http.delete(u + id + '/').pipe(
      catchError(this.handleError)
    );
  }

  protected handleError(error: HttpErrorResponse) {
    if (error.status === 400) {
      return throwError(new BadInput(error));
    }

    if (error.status === 404) {
      return throwError(new NotFoundError());
    }

    return throwError(new AppError(error));
  }
}
