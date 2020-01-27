import {async, ComponentFixture, TestBed} from '@angular/core/testing';

import {LoginComponent} from './login.component';
import {MatDividerModule, MatProgressSpinnerModule, MatSnackBar} from '@angular/material';
import {MdComponentsModule} from '@app/md-components/md-components.module';
import {BrowserModule} from '@angular/platform-browser';
import {FormBuilder, FormsModule, ReactiveFormsModule} from '@angular/forms';
import {HttpClientModule} from '@angular/common/http';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {ActivatedRoute, Router} from '@angular/router';
import {AuthenticationService} from '@services';
import {of} from 'rxjs';

describe('LoginComponent', () => {
  let component: LoginComponent;
  let fixture: ComponentFixture<LoginComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports: [MatDividerModule, MdComponentsModule, BrowserModule, FormsModule,
        ReactiveFormsModule, MatProgressSpinnerModule, HttpClientModule, BrowserAnimationsModule],
      declarations: [LoginComponent],
      providers: [FormBuilder,
        {
          provide: Router,
          useClass: class {
            navigate = jasmine.createSpy('navigate');
          }
        },
        AuthenticationService,
        MatSnackBar,
        {
          provide: ActivatedRoute,
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
              returnUrl: 'asdf',
              queryParams: 'asdf'
            }
          }
        }
      ]
    })
      .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LoginComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
