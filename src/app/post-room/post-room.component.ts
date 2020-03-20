import { Component, OnInit } from '@angular/core';
import { FormGroup,ReactiveFormsModule, FormBuilder,FormArray, Validators, FormControl,NgForm  } from '@angular/forms';
import { RoomServiceService } from '../room-service.service';
import { Room } from '../room'
import { Router } from '@angular/router';
@Component({
  selector: 'app-post-room',
  templateUrl: './post-room.component.html',
  styleUrls: ['./post-room.component.css']
})
export class PostRoomComponent implements OnInit {
  postRoomForm: FormGroup;
  constructor(private roomService: RoomServiceService, private formBuilder: FormBuilder){ }
  dataSaved = false;
  
  ngOnInit() {
    this.postRoomForm  =  this.formBuilder.group({
      name: ['', Validators.required],
      address: ['', Validators.required],
      city: ['', Validators.required],
      state: ['', Validators.required],
      bathroomCount: ['', Validators.required],
      bedCount: ['', Validators.required],
      guestCount: ['', Validators.required],
    });
  }
  postRoom(){
    var room: Room ;// new Room() 
    room = new Room()
    room.host = 1
    room.name = this.postRoomForm.value.name
    room.address = this.postRoomForm.value.address
    console.log("The state is " + this.postRoomForm.value.state)
    room.state = this.postRoomForm.value.state
    room.city = this.postRoomForm.value.city
    room.bath_count = this.postRoomForm.value.bathroomCount
    room.guest_count = this.postRoomForm.value.guestCount
    room.bed_count = this.postRoomForm.value.bedCount
    this.roomService.postRoom(room).subscribe(
      
      resp => { console.log(resp);this.dataSaved = true;
        
      },
      err => {
        console.log(err);
      }
    )
  }
}
