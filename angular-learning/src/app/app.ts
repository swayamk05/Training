import { Component } from '@angular/core';
import { UserForm } from './user-form/user-form';

@Component({
  selector: 'app-root',
  imports: [UserForm],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
}