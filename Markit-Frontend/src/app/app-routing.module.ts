import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { SignupComponent } from './signup/signup.component';
import { HomeComponent } from './home/home.component';
import {CalendarsComponent} from '@app/calendars/calendars.component';
import {NewCalendarComponent} from '@app/new-calendar/new-calendar.component';
import {PostsComponent} from '@app/posts/posts.component';
import {NewPostComponent} from '@app/new-post/new-post.component';
import {AuthGuard} from '@app/_helpers/auth.guard';
import {TwitterAuthComponent} from '@app/twitter-auth/twitter-auth.component';


const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'login', component: LoginComponent },
  { path: 'register', component: SignupComponent },
  { path: 'calendars/:id/create', component: NewPostComponent},
  { path: 'calendars/create', component: NewCalendarComponent},
  { path: 'calendars/:id', component: PostsComponent},
  { path: 'calendars', component: CalendarsComponent},
  // todo pathMatch:  'full'
  // todo canActivate: [AuthGuard]
  { path: 'twitter-auth', component: TwitterAuthComponent },
  // { path: 'no-access', component: }

  { path: '**', redirectTo: '' }// redirect to not found??
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
