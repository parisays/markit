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
import {HTTP_INTERCEPTORS, HttpClientModule} from '@angular/common/http';
import { DashboardComponent } from './dashboard/dashboard.component';
import { CalendarsComponent } from './calendars/calendars.component';
import { PostListViewComponent } from './post-list-view/post-list-view.component';
import { NewPostComponent } from './new-post/new-post.component';
import { TwitterAuthComponent } from './twitter-auth/twitter-auth.component';
import { HeaderComponent } from './header/header.component';
import { PostDetailsFormComponent } from './post-details-form/post-details-form.component';
import { AuthorizedHeaderComponent } from './authorized-header/authorized-header.component';
import { UnauthorizedHeaderComponent } from './unauthorized-header/unauthorized-header.component';
import { CalendarDetailsFormComponent } from './calendar-details-form/calendar-details-form.component';
import { SocialAccountsConnectionComponent } from './social-accounts-connection/social-accounts-connection.component';
import { CalendarWizardComponent } from './calendar-wizard/calendar-wizard.component';
import { PostIdeasComponent } from './post-ideas/post-ideas.component';
import { SocialChannelsSelectionComponent } from './social-channels-selection/social-channels-selection.component';
import { BasePostContentComponent } from './base-post-content/base-post-content.component';
import { PostWizardComponent } from './post-wizard/post-wizard.component';
import {AuthInterceptor} from '@app/_helpers/auth.interceptor';
import { ManualTestComponent } from './manual-test/manual-test.component';
import { CalendarSettingsComponent } from './calendar-settings/calendar-settings.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    SignupComponent,
    DashboardComponent,
    HeaderComponent,
    CalendarsComponent,
    PostListViewComponent,
    NewPostComponent,
    TwitterAuthComponent,
    PostDetailsFormComponent,
    AuthorizedHeaderComponent,
    UnauthorizedHeaderComponent,
    CalendarDetailsFormComponent,
    SocialAccountsConnectionComponent,
    CalendarWizardComponent,
    ManualTestComponent,
    PostIdeasComponent,
    SocialChannelsSelectionComponent,
    BasePostContentComponent,
    PostWizardComponent,
    CalendarSettingsComponent,
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
    MatProgressSpinnerModule,
  ],
  providers: [
    { provide: HTTP_INTERCEPTORS, useClass: AuthInterceptor, multi: true }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
