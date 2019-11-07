import { Component, OnInit } from '@angular/core';
import { AuthenticationService } from '@services';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'app-authorized-header',
  templateUrl: './authorized-header.component.html',
  styleUrls: ['./authorized-header.component.scss']
})
export class AuthorizedHeaderComponent implements OnInit {

  constructor(
    private authService: AuthenticationService,
    private http: HttpClient,
    private router: Router) { }

  ngOnInit() {
  }

}
