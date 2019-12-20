import { NgModule } from '@angular/core';

import {MatFormFieldModule} from '@angular/material/form-field';
import {MatIconModule} from '@angular/material/icon';
import {MatInputModule} from '@angular/material/input';
import {MatButtonModule} from '@angular/material/button';
import {MatListModule} from '@angular/material/list';
import {MatTableModule} from '@angular/material/table';
import {MatMenuModule} from '@angular/material/menu';
import {MatStepperModule} from '@angular/material/stepper';
import {MatRippleModule, MatNativeDateModule} from '@angular/material/core';
import {MatSelectModule} from '@angular/material/select';
import {MatDatepickerModule} from '@angular/material/datepicker';

@NgModule({
  exports: [
    MatFormFieldModule,
    MatIconModule,
    MatInputModule,
    MatButtonModule,
    MatListModule,
    MatTableModule,
    MatMenuModule,
    MatStepperModule,
    MatRippleModule,
    MatSelectModule,
    MatDatepickerModule,
    MatNativeDateModule
  ]
})
export class MdComponentsModule { }
