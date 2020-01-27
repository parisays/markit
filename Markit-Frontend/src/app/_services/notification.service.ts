import { Injectable } from '@angular/core';
import {webSocket} from 'rxjs/webSocket';
import {Notification} from '@models';
import {AuthenticationService} from '@app/_services/auth.service';
import {from, Observable, of, BehaviorSubject} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class NotificationService {
  ws = webSocket('');
  notifs: Notification[] = [
    {
      id: 1,
      type: 'invitation',
      title: 'New Invitation!',
      text: 'You\'ve been invited to calendar cal2',
      additionalData: {
        token: 'fasdf'
      }
    },
    {
      id: 2,
      type: 'comment',
      title: 'New Comment!',
      text: '[username] commented on post [post title]',
      additionalData: {
        calendarId: 12,
        postId: 414
      }
    },
    {
      id: 3,
      type: 'edit_post',
      title: 'Post Edit',
      text: '[username] edited post [post title]',
      additionalData: {
        calendarId: 122,
        postId: 4114
      }
    },
  ];

  notifsSubject: BehaviorSubject<Notification[]>;

  constructor(private authService: AuthenticationService) {
    this.notifsSubject = new BehaviorSubject<Notification[]>(this.notifs);

    const wsUrl = `ws://178.63.149.140:8000/ws/notification/${this.authService.currentUserValue.key}/`;
    this.ws = webSocket(wsUrl);
    // TODO subscribe ws
  }

  getNotifications(): Observable<Notification[]> {
    return this.notifsSubject.asObservable();
  }

  // getNotificationsCount(): Observable<number> {
  //   return this.;
  // }

  seenNotification(notifId: number): void {
    // TODO req set seen
    const nf = this.notifsSubject.getValue();
    nf.splice(nf.findIndex(n => n.id === notifId), 1);
    this.notifsSubject.next(nf);
  }
}
