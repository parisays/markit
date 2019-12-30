import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CollaboratorInvitationFormComponent } from './collaborator-invitation-form.component';

describe('CollaboratorInvitationFormComponent', () => {
  let component: CollaboratorInvitationFormComponent;
  let fixture: ComponentFixture<CollaboratorInvitationFormComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CollaboratorInvitationFormComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CollaboratorInvitationFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
