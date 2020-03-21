import { Component, OnInit, Input} from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { RoomService } from '../../room.service'
import { Room } from '../../room'
import { Reservation } from '../../reservation'
import { BookingsService } from '../../bookings.service'

@Component({
  selector: 'app-room-detail',
  templateUrl: './room-detail.component.html',
  styleUrls: ['./room-detail.component.css']
})
export class RoomDetailComponent implements OnInit {
  @Input() room:Room;
  constructor(private route: ActivatedRoute, private roomService: RoomService, private bookingService: BookingsService) { }
  
  roomID: number;
  startDate: Date;
  endDate: Date;
  
  static formatDate(date:Date) {
    var d = new Date(date),
        month = '' + (d.getMonth() + 1),
        day = '' + d.getDate(),
        year = d.getFullYear();

    if (month.length < 2) 
        month = '0' + month;
    if (day.length < 2) 
        day = '0' + day;

    return [year, month, day].join('-');
  }

  getRoom(): void {
    const id = +this.route.snapshot.paramMap.get('id');
    this.roomService.getRoom(id)
      .subscribe(room => (console.log("WHDFDFY " + room.name),this.room = room));
  }

  ngOnInit() {
    this.roomID = +this.route.snapshot.paramMap.get('id');
    this.getRoom()
  }

  make_booking(){
    var reservation: Reservation = new Reservation(this.roomID, RoomDetailComponent.formatDate(this.startDate), RoomDetailComponent.formatDate(this.endDate))
  
    this.bookingService.bookRoom(reservation).subscribe(
        resp => {console.log("The response is " + resp.toString) 
      },
      err => {
        console.log(err);
      }
    )
  }

}
