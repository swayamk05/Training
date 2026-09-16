import { Component } from '@angular/core';
import {
  FormControl,
  FormGroup,
  ReactiveFormsModule,
  Validators
} from '@angular/forms';

@Component({
  selector: 'app-user-form',
  imports: [ReactiveFormsModule],
  templateUrl: './user-form.html',
  styleUrl: './user-form.css'
})
export class UserForm {

  userForm = new FormGroup({
    name: new FormControl('', Validators.required),
    email: new FormControl('', Validators.required)
  });

  save() {
    console.log(this.userForm.value);
  }

  sayHello() {
    const name = this.userForm.value.name;
    alert(`HEllo, ${name}`);
  }
}