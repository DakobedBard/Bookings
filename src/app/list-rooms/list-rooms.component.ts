import { Component, OnInit } from '@angular/core';
import { BookingsService } from '../bookings.service';
import { Listing } from '../listing'

@Component({
  selector: 'app-list-rooms',
  templateUrl: './list-rooms.component.html',
  styleUrls: ['./list-rooms.component.css']
})

export class ListRoomsComponent implements OnInit {

  constructor(private bookingServie: BookingsService) { }
  listings: any = [];
  ngOnInit() {
    this.getRoomsListing()
  }
  getRoomsListing(){
    this.bookingServie.getListings().subscribe(
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
