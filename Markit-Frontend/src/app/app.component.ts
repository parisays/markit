import {Component} from '@angular/core';
import {AuthenticationService, CalendarService} from '@services';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'Markit';

  constructor(public  authService: AuthenticationService) {
  }
}
