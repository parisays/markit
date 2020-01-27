import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SignupComponent } from './signup.component';
import { FormBuilder, FormsModule, ReactiveFormsModule } from '@angular/forms';
import { ActivatedRoute, Router, convertToParamMap } from '@angular/router';
import { AuthenticationService } from '@services';
import { MatSnackBar, MatDivider, MatDividerModule, MatSpinner, MatProgressSpinnerModule } from '@angular/material';

import 'zone.js/dist/zone-testing';
import { MdComponentsModule } from '@app/md-components/md-components.module';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { Observable, of, from } from 'rxjs';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

export class ActivatedRouteMock {
  public paramMap = of(convertToParamMap({
      returnUrl: 'abc123',
      queryParams: from([{id: 1}]),
  }));
}

fdescribe('SignupComponent', () => {
  let component: SignupComponent;
  let fixture: ComponentFixture<SignupComponent>;

  const fakeActivatedRoute = {
    // snapshot: { queryParams: from([{id: 1}] }
  } as ActivatedRoute;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports: [ MatDividerModule, MdComponentsModule, BrowserModule,
        FormsModule,
        ReactiveFormsModule, MatProgressSpinnerModule, HttpClientModule, BrowserAnimationsModule ],
      declarations: [ SignupComponent ],
      providers: [ FormBuilder,
        {
          provide: Router,
          useClass: class { navigate = jasmine.createSpy("navigate"); }
        },
        AuthenticationService,
        MatSnackBar,
        {provide: ActivatedRoute,
          useValue: { // Mock
            queryParams: of(
              {
                id_params: 'id_params_test'
              }
            ),
            params: of(
              {
                id_query_params: 'id_query_params_test'
              }
            ),
            snapshot: {
              returnUrl: "asdf",
              queryParams: "asdf"
            }
          }
        }
        ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SignupComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
