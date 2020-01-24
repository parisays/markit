import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';
import { MdComponentsModule } from './md-components/md-components.module';
import { MatSnackBarModule } from '@angular/material/snack-bar';
import { SignupComponent } from './signup/signup.component';
import {MatCardModule, MatListModule, MatProgressSpinnerModule, MatTabsModule, MatToolbarModule} from '@angular/material';
import {HTTP_INTERCEPTORS, HttpClientModule} from '@angular/common/http';
import { DashboardComponent } from './dashboard/dashboard.component';
import { CalendarListViewComponent } from './calendar-list-view/calendar-list-view.component';
import { PostListViewComponent } from './post-list-view/post-list-view.component';
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
import { PostOverviewSimpleComponent } from './post-overview-simple/post-overview-simple.component';
import { HomepageComponent } from './homepage/homepage.component';
import { ProfileComponent } from './profile/profile.component';
import { CollaboratorInvitationFormComponent } from './collaborator-invitation-form/collaborator-invitation-form.component';
import { TimepickerModule } from 'ngx-bootstrap/timepicker';
import { ForgetPassComponent } from './forget-pass/forget-pass.component';
import { ResetPassComponent } from './reset-pass/reset-pass.component';
import { NotificationDialogComponent } from './notification-dialog/notification-dialog.component';
import { NgZorroAntdModule, NZ_I18N, en_US } from 'ng-zorro-antd';
import { registerLocaleData } from '@angular/common';
import en from '@angular/common/locales/en';
import { CommentComponent } from './comment/comment.component';
import { NzCommentModule } from 'ng-zorro-antd/comment';
import { PostPreviewComponent } from './post-preview/post-preview.component';
import { NzAvatarModule } from 'ng-zorro-antd/avatar';
import { CalendarViewComponent } from './calendar-view/calendar-view.component';
import { NzCalendarModule } from 'ng-zorro-antd/calendar';
import { NzIconModule } from 'ng-zorro-antd/icon';
import { PostStatusComponent } from './post-status/post-status.component';
import { QuickLinksComponent } from './quick-links/quick-links.component';
registerLocaleData(en);

@NgModule({
  entryComponents: [
    NotificationDialogComponent,
  ],
  declarations: [
    AppComponent,
    LoginComponent,
    SignupComponent,
    DashboardComponent,
    HeaderComponent,
    CalendarListViewComponent,
    PostListViewComponent,
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
    PostOverviewSimpleComponent,
    HomepageComponent,
    ProfileComponent,
    CollaboratorInvitationFormComponent,
    ForgetPassComponent,
    ResetPassComponent,
    NotificationDialogComponent,
    CommentComponent,
    PostPreviewComponent,
    CalendarViewComponent,
    NotificationDialogComponent,
    PostStatusComponent,
    QuickLinksComponent,
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
    TimepickerModule.forRoot(),
    NgZorroAntdModule,
    FormsModule,
    NzCommentModule,
    NzAvatarModule,
    NzCalendarModule,
    NzIconModule,
  ],
  providers: [
    { provide: HTTP_INTERCEPTORS, useClass: AuthInterceptor, multi: true },
    { provide: NZ_I18N, useValue: en_US }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
