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
  constructor(
    public dialogRef: MatDialogRef<NotificationDialogComponent>,
    @Inject(MAT_DIALOG_DATA) public data: Notification[],
    private collaborationService: CollaborationService,
    private snackBar: MatSnackBar) {
  }

  ngOnInit() {
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
    }, () => {
      this.dialogRef.close();
    });
  }

  onReject(token: string) {
    // TODO remove notif
    this.data.splice(this.data.findIndex(n => n.token === token));
    this.dialogRef.close();
  }
}
