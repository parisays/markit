import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {LoginComponent} from './login/login.component';
import {SignupComponent} from './signup/signup.component';
import {CalendarListViewComponent} from '@app/calendar-list-view/calendar-list-view.component';
import {PostListViewComponent} from '@app/post-list-view/post-list-view.component';
import {AuthGuard} from '@app/_helpers/auth.guard';
import {TwitterAuthComponent} from '@app/twitter-auth/twitter-auth.component';
import {DashboardComponent} from './dashboard/dashboard.component';
import {CalendarWizardComponent} from '@app/calendar-wizard/calendar-wizard.component';
import {PostWizardComponent} from '@app/post-wizard/post-wizard.component';
import { HomepageComponent } from './homepage/homepage.component';
import {CalendarSettingsComponent} from '@app/calendar-settings/calendar-settings.component';


const routes: Routes = [
  {path: '', component: HomepageComponent},
  // {path: '', component: DashboardComponent, canActivate: [AuthGuard]},
  {path: 'login', component: LoginComponent},
  {path: 'register', component: SignupComponent},
  {path: 'twitter-auth', component: TwitterAuthComponent},

  {path: 'calendars/:calendarId/posts/new', component: PostWizardComponent, canActivate: [AuthGuard]},
  {path: 'calendars/:calendarId/posts/:postId/edit', component: PostWizardComponent, canActivate: [AuthGuard]},
  {path: 'calendars/:calendarId/posts', component: PostListViewComponent, canActivate: [AuthGuard]},

  {path: 'calendars/:calendarId/edit', redirectTo: 'calendars/:calendarId/wizard/details', canActivate: [AuthGuard]},

  {path: 'calendars/new', component: CalendarWizardComponent, canActivate: [AuthGuard]},
  {path: 'calendars/:calendarId/wizard/details', component: CalendarWizardComponent, canActivate: [AuthGuard]},
  {path: 'calendars/:calendarId/wizard/social-accounts', component: CalendarWizardComponent, canActivate: [AuthGuard]},
  {path: 'calendars/:calendarId/wizard', redirectTo: 'calendars/:calendarId/wizard/details', canActivate: [AuthGuard]},

  {path: '**', redirectTo: ''}// redirect to not found??
  // todo pathMatch:  'full'
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}
