import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PostIdeasComponent } from './post-ideas.component';

describe('PostIdeasComponent', () => {
  let component: PostIdeasComponent;
  let fixture: ComponentFixture<PostIdeasComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PostIdeasComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PostIdeasComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
