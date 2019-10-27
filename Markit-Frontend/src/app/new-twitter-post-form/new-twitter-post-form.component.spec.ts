import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { NewTwitterPostFormComponent } from './new-twitter-post-form.component';

describe('NewTwitterPostFormComponent', () => {
  let component: NewTwitterPostFormComponent;
  let fixture: ComponentFixture<NewTwitterPostFormComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ NewTwitterPostFormComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(NewTwitterPostFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
