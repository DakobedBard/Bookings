import { Component, OnInit, Input} from '@angular/core';
import { Room } from '../../room'
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import { RoomService } from '../../room.service'
@Component({
  selector: 'app-room-detail',
  templateUrl: './room-detail.component.html',
  styleUrls: ['./room-detail.component.css']
})
export class RoomDetailComponent implements OnInit {
  @Input() room: Room;
  constructor(    private route: ActivatedRoute,
    private heroService: RoomService,
    private location: Location
    ) { }

  ngOnInit() {
    this.getRoom();
  }

  getRoom(): void {
    const id = +this.route.snapshot.paramMap.get('id');
    this.heroService.getRoom(id)
      .subscribe(room => this.room = room);
  }
  
  goBack(): void {
    this.location.back();
  }
}

