import {Component, Input, OnInit} from '@angular/core';
import { Validators, FormGroup, FormBuilder } from '@angular/forms';
import {CollaborationService} from '@app/_services/collaboration.service';
import {MatSnackBar} from '@angular/material';

@Component({
  selector: 'app-collaborator-invitation-form',
  templateUrl: './collaborator-invitation-form.component.html',
  styleUrls: ['./collaborator-invitation-form.component.scss']
})
export class CollaboratorInvitationFormComponent implements OnInit {
  @Input() calendarId: number;

  form: FormGroup = this.fb.group({
    email: ['', [
      Validators.email,
      Validators.required
    ]],
    role_name: ['Viewer']
  });

  hasData = true;
  loading = false;
  notFound = false;
  displayedColumns: string[] = ['logo', 'email', 'role'];

  roles = ['Owner', 'Manager', 'Viewer', 'Editor'];

  collaborators: { email: string, role_name: string }[] = [];

  constructor(private fb: FormBuilder,
              private collaborationService: CollaborationService,
              private snackBar: MatSnackBar) { }

  get f() { return this.form.controls; }

  ngOnInit() {
  }

  onInvite() {
    if (this.form.invalid) {
      return;
    }

    this.loading = true;

    const r = {
      email: this.f.email.value,
      calendar: this.calendarId.toString(),
      role_name: this.f.role_name.value,
    };

    this.collaborationService.create(r).subscribe((res: { email: string, role_name: string }) => {
      console.log(res);
      this.snackBar.open(`Invitation sent to ${res.email}`, 'Dismiss', {duration: 2000});
      this.updateInvitationList();
    }, error => {
      console.log(error);
      this.snackBar.open(`Invitation failed`, 'Dismiss', {duration: 2000});
    }, () => {
      this.loading = false;
    });
  }

  private updateInvitationList() {
    // this.collaborationService.getAll() : TODO
  }
}
