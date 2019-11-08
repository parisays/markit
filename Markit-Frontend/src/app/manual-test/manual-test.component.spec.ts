import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ManualTestComponent } from './manual-test.component';

describe('ManualTestComponent', () => {
  let component: ManualTestComponent;
  let fixture: ComponentFixture<ManualTestComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ManualTestComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ManualTestComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
