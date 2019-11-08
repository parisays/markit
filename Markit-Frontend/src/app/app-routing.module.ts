import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {LoginComponent} from './login/login.component';
import {SignupComponent} from './signup/signup.component';
import {CalendarListViewComponent} from '@app/calendar-list-view/calendar-list-view.component';
import {PostListViewComponent} from '@app/post-list-view/post-list-view.component';
import {NewPostComponent} from '@app/new-post/new-post.component';
import {AuthGuard} from '@app/_helpers/auth.guard';
import {TwitterAuthComponent} from '@app/twitter-auth/twitter-auth.component';
import {DashboardComponent} from './dashboard/dashboard.component';
import {CalendarWizardComponent} from '@app/calendar-wizard/calendar-wizard.component';
import {PostWizardComponent} from '@app/post-wizard/post-wizard.component';


const routes: Routes = [
  // {path: '', component:HomePageComponent}
  {path: '', component: DashboardComponent, canActivate: [AuthGuard]},
  {path: 'login', component: LoginComponent},
  {path: 'register', component: SignupComponent},
  {path: 'twitter-auth', component: TwitterAuthComponent},

  {path: 'calendars/:calendarId/posts/new', component: PostWizardComponent, canActivate: [AuthGuard]},
  {path: 'calendars/:calendarId/posts/:postId/edit', component: PostWizardComponent, canActivate: [AuthGuard]},
  // { path: 'calendars/:calendarId/posts', component: PostsListComponent, canActivate: [AuthGuard]},

  {path: 'calendars/new', component: CalendarWizardComponent, canActivate: [AuthGuard]},
  {path: 'calendars/:calendarId/wizard', redirectTo: 'calendars/:calendarId/wizard/details', canActivate: [AuthGuard]},
  /*children: [*/
  {path: 'calendars/:calendarId/wizard/details', component: CalendarWizardComponent, canActivate: [AuthGuard]},
  {path: 'calendars/:calendarId/wizard/social-accounts', component: CalendarWizardComponent, canActivate: [AuthGuard]},

  {path: 'calendars/:calendarId/posts', component: PostListViewComponent, canActivate: [AuthGuard]},

  // { path: 'calendars/:calendarId/edit', component: CalendarsSettingsComponent, canActivate: [AuthGuard]},

  // todo pathMatch:  'full'
  {path: '**', redirectTo: ''}// redirect to not found??
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}
