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
import {MatCardModule, MatListModule, MatProgressSpinnerModule, MatTabsModule, MatToolbarModule} from '@angular/material';
import {HttpClientModule} from '@angular/common/http';
import { DashboardComponent } from './dashboard/dashboard.component';
import { CalendarsComponent } from './calendars/calendars.component';
import { NewCalendarComponent } from './new-calendar/new-calendar.component';
import { PostsComponent } from './posts/posts.component';
import { NewPostComponent } from './new-post/new-post.component';
import { TwitterAuthComponent } from './twitter-auth/twitter-auth.component';
import { HeaderComponent } from './header/header.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    SignupComponent,
    DashboardComponent,
    HeaderComponent,
    DashboardComponent,
    CalendarsComponent,
    NewCalendarComponent,
    PostsComponent,
    NewPostComponent,
    TwitterAuthComponent
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
