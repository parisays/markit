import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BasePostContentComponent } from './base-post-content.component';

describe('BasePostContentComponent', () => {
  let component: BasePostContentComponent;
  let fixture: ComponentFixture<BasePostContentComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BasePostContentComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BasePostContentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
