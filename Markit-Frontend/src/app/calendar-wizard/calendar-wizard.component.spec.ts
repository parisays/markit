import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CalendarWizardComponent } from './calendar-wizard.component';

describe('CalendarWizardComponent', () => {
  let component: CalendarWizardComponent;
  let fixture: ComponentFixture<CalendarWizardComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CalendarWizardComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CalendarWizardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
