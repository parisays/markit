import {Component, Inject, OnInit} from '@angular/core';
import {MatDialogRef, MAT_DIALOG_DATA} from '@angular/material/dialog';
import {CollaborationService} from '@app/_services/collaboration.service';
import {MatSnackBar} from '@angular/material';
import {BehaviorSubject, Observer} from 'rxjs';
import {Notification} from '@app/_models/notification';
import {NotificationService} from '@app/_services/notification.service';
import {Router} from '@angular/router';

@Component({
  selector: 'app-notification-dialog',
  templateUrl: './notification-dialog.component.html',
  styleUrls: ['./notification-dialog.component.scss']
})
export class NotificationDialogComponent implements OnInit {

  // dataSubject: BehaviorSubject<Notification[]> = new BehaviorSubject<Notification[]>([]);
  data: Notification[];

  constructor(
    private collaborationService: CollaborationService,
    private snackBar: MatSnackBar,
    private notificationService: NotificationService,
    private router: Router) {
    this.notificationService.getNotifications().subscribe(n => {
      console.log(n);
      this.data = n;
    });
  }

  ngOnInit() {

  }

  onAccept(notifId: number, token: string) {
    this.collaborationService.activate(token).subscribe(res => {
      console.log(res);
      this.snackBar.open('Successfully added to calendar', 'Dismiss', {duration: 2000});
      this.notificationService.seenNotification(notifId);
    }, err => {
      console.log(err);
      this.snackBar.open('Operation failed', 'Dismiss', {duration: 2000});
    });
  }

  onReject(notifId: number) {
    this.notificationService.seenNotification(notifId);
  }

  onCheckPost(notifId: number, calendarId: number, postId: number) {
    this.router.navigate(['calendars', calendarId, 'posts', postId, 'preview']);
    this.notificationService.seenNotification(notifId);
  }

  onSeen(notifId: number) {
    this.notificationService.seenNotification(notifId);
  }
}
