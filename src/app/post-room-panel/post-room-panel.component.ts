import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-post-room-panel',
  templateUrl: './post-room-panel.component.html',
  styleUrls: ['./post-room-panel.component.css']
})
export class PostRoomPanelComponent implements OnInit {
  panelOpenState = false;
  constructor() { }

  ngOnInit() {
  }

}
