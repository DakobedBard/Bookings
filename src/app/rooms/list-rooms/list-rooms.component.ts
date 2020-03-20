import { Component, OnInit } from '@angular/core';
import { Listing } from '../../listing'
import { RoomService } from '../../room.service'


@Component({
  selector: 'app-list-rooms',
  templateUrl: './list-rooms.component.html',
  styleUrls: ['./list-rooms.component.css']
})

export class ListRoomsComponent implements OnInit {

  constructor(private roomService: RoomService) { }
  listings: any = [];
  ngOnInit() {
    this.getRoomsListing()
  }
  getRoomsListing(){
    this.roomService.getRooms().subscribe(
      (data) => {
        for (const listing of (data as any)) {
          this.listings.push(new Listing(listing.id, listing.city, listing.state, listing.guest_count, listing.name))
        }
      },
      (err) => {  
        console.log(err);
      }
    );
  }

}
