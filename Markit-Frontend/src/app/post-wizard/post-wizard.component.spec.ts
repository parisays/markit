import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PostWizardComponent } from './post-wizard.component';

describe('PostWizardComponent', () => {
  let component: PostWizardComponent;
  let fixture: ComponentFixture<PostWizardComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PostWizardComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PostWizardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
