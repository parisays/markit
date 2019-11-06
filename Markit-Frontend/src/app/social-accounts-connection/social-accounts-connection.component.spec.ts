import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SocialAccountsConnectionComponent } from './social-accounts-connection.component';

describe('SocialAccountsConnectionComponent', () => {
  let component: SocialAccountsConnectionComponent;
  let fixture: ComponentFixture<SocialAccountsConnectionComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SocialAccountsConnectionComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SocialAccountsConnectionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
