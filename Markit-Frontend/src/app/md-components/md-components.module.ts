import { NgModule } from '@angular/core';

import {MatFormFieldModule} from '@angular/material/form-field';
import {MatIconModule} from '@angular/material/icon';
import {MatInputModule} from '@angular/material/input';
import {MatButtonModule} from '@angular/material/button';
import {MatListModule} from '@angular/material/list';
import {MatTableModule} from '@angular/material/table';

@NgModule({
  exports: [
    MatFormFieldModule,
    MatIconModule,
    MatInputModule,
    MatButtonModule,
    MatListModule,
    MatTableModule
  ]
})
export class MdComponentsModule { }
