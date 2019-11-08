import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PostOverviewSimpleComponent } from './post-overview-simple.component';

describe('PostOverviewSimpleComponent', () => {
  let component: PostOverviewSimpleComponent;
  let fixture: ComponentFixture<PostOverviewSimpleComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PostOverviewSimpleComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PostOverviewSimpleComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
