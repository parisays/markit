import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {BehaviorSubject, Observable, throwError} from 'rxjs';
import {map, timeout} from 'rxjs/operators';

import { environment } from '@environments/environment';
import { User } from '@models';

@Injectable({ providedIn: 'root' })
export class AuthenticationService {
    private currentUserSubject: BehaviorSubject<User>;
    public currentUser: Observable<User>;
    private loginEndpoint = `${environment.apiUrl}/api/v1.0/auth/rest-auth/login/`;
    private registerEndpoint = `${environment.apiUrl}/api/v1.0/auth/rest-auth/registration/`;

    constructor(private http: HttpClient) {
        this.currentUserSubject = new BehaviorSubject<User>(JSON.parse(localStorage.getItem('currentUser')));
        this.currentUser = this.currentUserSubject.asObservable();
    }

    public get currentUserValue(): User {
        return this.currentUserSubject.value;
    }

    login(email: string, password: string) {
        return this.http.post<any>(this.loginEndpoint, { email, password })
          .pipe(
            timeout(10000),
            map(data => {
              if (data && data.key) {
                const newUser: User = { email, key: data.key };
                localStorage.setItem('currentUser', JSON.stringify(newUser));
                this.currentUserSubject.next(newUser);
                return newUser;
              } else {
                return throwError(new Error('invalid login response'));
              }
            })
          );
    }

    logout(): void {
        localStorage.removeItem('currentUser');
        this.currentUserSubject.next(null);
    }

    isLoggedIn(): boolean {
      return !!(this.currentUserValue);
    }

    register(
      email: string,
      password: string,
      firstName: string,
      lastName: string
    ) {
      return this.http.post<User>(this.registerEndpoint, {
        email,
        password1: password,
        password2: password,
        firstName,
        lastName,
      }).pipe(
        timeout(10000),
        map(data => {
          if (data && data.key) {
            const newUser: User = { email, key: data.key, firstName, lastName };
            localStorage.setItem('currentUser', JSON.stringify(newUser));
            this.currentUserSubject.next(newUser);
            return newUser;
          } else {
            return throwError(new Error('invalid login response'));
          }
        })
      );
    }
}
