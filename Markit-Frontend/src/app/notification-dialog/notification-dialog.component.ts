import {Component, Inject, OnInit} from '@angular/core';
import {MatDialogRef, MAT_DIALOG_DATA} from '@angular/material/dialog';
import {Notification} from '@app/authorized-header/authorized-header.component';
import {CollaborationService} from '@app/_services/collaboration.service';
import {MatSnackBar} from '@angular/material';

@Component({
  selector: 'app-notification-dialog',
  templateUrl: './notification-dialog.component.html',
  styleUrls: ['./notification-dialog.component.scss']
})
export class NotificationDialogComponent implements OnInit {

  data: Notification[];
  constructor(
    private collaborationService: CollaborationService,
    private snackBar: MatSnackBar) {
  }

  ngOnInit() {
    // this.data = [
    //   {
    //     type: 'notif',
    //     calendar: 7478723,
    //     token: 'jhdf',
    //     invited: 3840,
    //     inviter: 3749327,
    //   },
    //   {
    //     type: 'notif',
    //     calendar: 7478723,
    //     token: 'jhdf',
    //     invited: 3840,
    //     inviter: 3749327,
    //   },
    //   {
    //     type: 'notif',
    //     calendar: 7478723,
    //     token: 'jhdf',
    //     invited: 3840,
    //     inviter: 3749327,
    //   },
    //   {
    //     type: 'notif',
    //     calendar: 7478723,
    //     token: 'jhdf',
    //     invited: 3840,
    //     inviter: 3749327,
    //   },
    //   {
    //     type: 'notif',
    //     calendar: 7478723,
    //     token: 'jhdf',
    //     invited: 3840,
    //     inviter: 3749327,
    //   }
    // ];
  }

  onAccept(token: string) {
    this.collaborationService.activate(token).subscribe(res => {
      console.log(res);
      this.snackBar.open('Successfully added to calendar', 'Dismiss', {duration : 2000});
      // TODO remove notif
      this.data.splice(this.data.findIndex(n => n.token === token));
    }, err => {
      console.log(err);
      this.snackBar.open('Operation failed', 'Dismiss', {duration : 2000});
    });
  }

  onReject(token: string) {
    // TODO remove notif
    this.data.splice(this.data.findIndex(n => n.token === token));
  }
}
