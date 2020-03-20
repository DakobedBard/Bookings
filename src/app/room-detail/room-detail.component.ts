import { Component, OnInit, Input} from '@angular/core';
import { Listing } from '../listing'
@Component({
  selector: 'app-room-detail',
  templateUrl: './room-detail.component.html',
  styleUrls: ['./room-detail.component.css']
})
export class RoomDetailComponent implements OnInit {
  @Input() listing: Listing;
  constructor() { }

  ngOnInit() {
  
  }
}
