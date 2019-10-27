import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { NewCalendarFormComponent } from './new-calendar-form.component';

describe('NewCalendarFormComponent', () => {
  let component: NewCalendarFormComponent;
  let fixture: ComponentFixture<NewCalendarFormComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ NewCalendarFormComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(NewCalendarFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
