import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ReactiveFormsModule } from '@angular/forms';
import { MdComponentsModule } from './md-components/md-components.module';
import { SignupComponent } from './signup/signup.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { NewCalendarFormComponent } from './new-calendar-form/new-calendar-form.component';
import { NewTwitterPostFormComponent } from './new-twitter-post-form/new-twitter-post-form.component';
import { PostListComponent } from './post-list/post-list.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    SignupComponent,
    DashboardComponent,
    NewCalendarFormComponent,
    NewTwitterPostFormComponent,
    PostListComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    ReactiveFormsModule,
    MdComponentsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
