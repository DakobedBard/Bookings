import { Component, OnInit } from '@angular/core';
import { FormGroup,ReactiveFormsModule, FormBuilder,FormArray, Validators, FormControl,NgForm  } from '@angular/forms';

@Component({
  selector: 'app-post-room-details',
  templateUrl: './post-room-details.component.html',
  styleUrls: ['./post-room-details.component.css']
})
export class PostRoomDetailsComponent implements OnInit {

  constructor(private formBuilder: FormBuilder) { }

  ngOnInit() {
  }

}
