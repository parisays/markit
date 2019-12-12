import { Component, OnInit } from '@angular/core';
import { Validators, FormGroup, FormBuilder } from '@angular/forms';

@Component({
  selector: 'app-collaborator-invitation-form',
  templateUrl: './collaborator-invitation-form.component.html',
  styleUrls: ['./collaborator-invitation-form.component.scss']
})
export class CollaboratorInvitationFormComponent implements OnInit {

  form: FormGroup = this.fb.group({
    email: ['', [
      Validators.email,
      Validators.required
    ]]
  });

  hasData = true;
  
  displayedColumns: string[] = ['logo', 'email', 'role'];

  roles = ['owner', 'manager', 'viewer', 'editor'];

  collaborators = [
    {
      email: 'mjdfjk@kjdf.com',
      role: 'Owner'
    },
    {
      email: 'kfvkj@kjdf.com',
      role: 'Manager'
    },
    {
      email: 'dhd@kjdf.com',
      role: 'Editor'
    },
    {
      email: 'sfksjf@kjdf.com',
      role: 'Viewer'
    },
  ];

  constructor(private fb: FormBuilder) { }

  get f() { return this.form.controls; }

  ngOnInit() {
  }

}
