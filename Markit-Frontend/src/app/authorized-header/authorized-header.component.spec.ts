import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AutorizedHeaderComponent } from './authorized-header.component';

describe('AutorizedHeaderComponent', () => {
  let component: AutorizedHeaderComponent;
  let fixture: ComponentFixture<AutorizedHeaderComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AutorizedHeaderComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AutorizedHeaderComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
