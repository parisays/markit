import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SocialChannelsSelectionComponent } from './social-channels-selection.component';

describe('SocialChannelsSelectionComponent', () => {
  let component: SocialChannelsSelectionComponent;
  let fixture: ComponentFixture<SocialChannelsSelectionComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SocialChannelsSelectionComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SocialChannelsSelectionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
