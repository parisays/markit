import { Component, OnInit, ViewChild } from '@angular/core';
import { AuthenticationService } from '@services';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import {MatDialog} from '@angular/material';
import {NotificationDialogComponent} from '@app/notification-dialog/notification-dialog.component';
import { webSocket } from 'rxjs/webSocket';
import {WebSocketSubject} from 'rxjs/src/internal/observable/dom/WebSocketSubject';

@Component({
  selector: 'app-authorized-header',
  templateUrl: './authorized-header.component.html',
  styleUrls: ['./authorized-header.component.scss']
})
export class AuthorizedHeaderComponent implements OnInit {
  @ViewChild('notification', {static: false}) Notification: NotificationDialogComponent;

  ws = webSocket('');
  notifs: Notification[] = [];
  visible: boolean;
  count = 5;

  constructor(
    public authService: AuthenticationService,
    private http: HttpClient,
    private router: Router,
    private notifDialog: MatDialog) { }

  ngOnInit() {
    const wsUrl = `ws://178.63.149.140:8000/ws/notification/${this.authService.currentUserValue.key}/`;
    this.ws = webSocket(wsUrl);
    this.ws.subscribe((notif: Notification) => {
      console.log('notif', notif);
      this.notifs.push(notif);
    });
  }

  clickMe(): void {
    this.visible = false;
  }

  showNotifs() {
    // this.count++;
    console.log('show notif button clicked!' + this.count);
    this.Notification.data = this.notifs;
  }
}

export interface Notification {
  type: string;
  token: string;
  invited: number;
  inviter: number;
  calendar: number;
}
