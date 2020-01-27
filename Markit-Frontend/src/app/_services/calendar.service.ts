import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';

import {environment} from '@environments/environment';
import { DataService } from './data.service';
import {Observable} from 'rxjs';
import { switchMap, map } from 'rxjs/operators';
import { Calendar, Access } from '@models';

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

  getMyAccess(id): Observable<object> {
    return this.get(id).pipe(
      map((cal: Calendar) => {
        const acc = cal.access;
        const accObj = this.mapAccess(acc);
        return accObj;
      })
    );
  }


  private mapAccess(backAcc: string[]): any {
    const accessObj = {
      canAddCollaborator: false,
      canEditCalendar: false,
      canDeleteCalendar: false,
      canCreatePost: false,
      canEditPost: false,
      canDeletePost: false,
      canSetPublish: false,
      canPostComment: false,
    };

    if (!backAcc) {
      return accessObj;
    }

    for (const acc of backAcc) {
      switch (acc) {
        case Access.ADD_COLLABORATOR: {
          accessObj.canAddCollaborator = true;
          break;
        }
        case Access.CREATE_POST: {
          accessObj.canCreatePost = true;
          break;
        }
        case Access.DELETE_CALENDAR: {
          accessObj.canDeleteCalendar = true;
          break;
        }
        case Access.DELETE_POST: {
          accessObj.canDeletePost = true;
          break;
        }
        case Access.EDIT_CALENDAR: {
          accessObj.canEditCalendar = true;
          break;
        }
        case Access.EDIT_POST: {
          accessObj.canEditPost = true;
          break;
        }
        case Access.POST_COMMENT: {
          accessObj.canPostComment = true;
          break;
        }
        case Access.SET_PUBLISH: {
          accessObj.canSetPublish = true;
          break;
        }
      }
    }

    return accessObj;
  }
}
