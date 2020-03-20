import { Component, OnInit } from '@angular/core';
import { Room } from '../../room'
import { RoomService } from '../../room.service'


@Component({
  selector: 'app-list-rooms',
  templateUrl: './list-rooms.component.html',
  styleUrls: ['./list-rooms.component.css']
})

export class ListRoomsComponent implements OnInit {

  constructor(private roomService: RoomService) { }
  rooms: any = [];
  ngOnInit() {
    this.getRoomsListing()
  }
  getRoomsListing(){
    this.roomService.getRooms().subscribe(
      (data) => {
        for (const room of (data as any)) {
          this.rooms.push(new Room(room.id, room.city, room.state, room.guest_count, room.name))
        }
      },
      (err) => {  
        console.log(err);
      }
    );
  }
}
