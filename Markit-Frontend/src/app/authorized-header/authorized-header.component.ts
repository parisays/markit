import {Component, OnInit, ViewChild} from '@angular/core';
import {AuthenticationService} from '@services';
import {HttpClient} from '@angular/common/http';
import {Router} from '@angular/router';
import {MatDialog} from '@angular/material';
import {NotificationDialogComponent} from '@app/notification-dialog/notification-dialog.component';
import {webSocket} from 'rxjs/webSocket';
import {Notification} from '@app/_models/notification';
import { NotificationService } from '@app/_services/notification.service';

@Component({
  selector: 'app-authorized-header',
  templateUrl: './authorized-header.component.html',
  styleUrls: ['./authorized-header.component.scss']
})
export class AuthorizedHeaderComponent implements OnInit {
  @ViewChild('notification', {static: false}) Notification: NotificationDialogComponent;

  visible: boolean;
  count = 0;

  constructor(
    public authService: AuthenticationService,
    private notificationService: NotificationService) {
      this.notificationService.getNotifications().subscribe(c => {
        this.count = c.length;
      });
  }

  ngOnInit() {
    // this.ws.subscribe((notif: Notification) => {
    //   console.log('notif', notif);
    //   this.notifs.push(notif);
    //   // this.notifs.next(this.notifs.getValue().concat([notif]));
    // });
  }

  clickMe(): void {
    // this.visible = false;
  }

  showNotifs() {
    // this.count++;
    // console.log('show notif button clicked!' + this.count);
    // this.Notification.dataSubject.next(this.notifs);
  }
}

