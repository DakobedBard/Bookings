import { Component, OnInit, Input} from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { RoomService } from '../../room.service'
import { Room } from '../../room'
@Component({
  selector: 'app-room-detail',
  templateUrl: './room-detail.component.html',
  styleUrls: ['./room-detail.component.css']
})
export class RoomDetailComponent implements OnInit {
  @Input() room:Room;
  constructor(private route: ActivatedRoute, private roomService: RoomService) { }

  getRoom(): void {
    const id = +this.route.snapshot.paramMap.get('id');
    console.log("The ID of the route is " + id)
    this.roomService.getRoom(id)
      .subscribe(room => this.room = room);
  }

  ngOnInit() {
    console.log("what ")
    this.getRoom()
  }
}
