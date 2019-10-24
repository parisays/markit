import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ReactiveFormsModule } from '@angular/forms';
import { MdComponentsModule } from './md-components/md-components.module';
import { MatSnackBarModule } from '@angular/material/snack-bar';
import { SignupComponent } from './signup/signup.component';
import { HomeComponent } from './home/home.component';
import {MatCardModule, MatListModule, MatProgressSpinnerModule, MatTabsModule, MatToolbarModule} from '@angular/material';
import {HttpClientModule} from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    SignupComponent,
    HomeComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    ReactiveFormsModule,
    MdComponentsModule,
    MatToolbarModule,
    MatTabsModule,
    HttpClientModule,
    MatListModule,
    MatCardModule,
    MatSnackBarModule,
    MatProgressSpinnerModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }