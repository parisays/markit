import { Injectable } from '@angular/core';
import { HttpRequest, HttpHandler, HttpEvent, HttpInterceptor } from '@angular/common/http';
import { Observable } from 'rxjs';

import { AuthenticationService } from '@services';

@Injectable()
export class AuthInterceptor implements HttpInterceptor {
  constructor(private authenticationService: AuthenticationService) { }

  intercept(request: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    // add authorization header with auth key if available
    const currentUser = this.authenticationService.currentUserValue;
    if (currentUser && currentUser.key) {
      request = request.clone({
        setHeaders: {
          Authorization: `Token ${currentUser.key}`
        }
      });
    }

    return next.handle(request);
  }
}
