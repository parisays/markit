import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { UnauthorizedHeaderComponent } from './unauthorized-header.component';

describe('UnauthorizedHeaderComponent', () => {
  let component: UnauthorizedHeaderComponent;
  let fixture: ComponentFixture<UnauthorizedHeaderComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ UnauthorizedHeaderComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(UnauthorizedHeaderComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
