import { Component, AfterViewInit, ViewChild, ElementRef } from "@angular/core";

@Component({
  selector: "app-root",
  templateUrl: "./app.component.html",
  styleUrls: ["./app.component.css"]
})
export class AppComponent implements AfterViewInit {
  tiles = [
    {text: 'One', cols: 3, rows: 8, color: '#142A5C'},
    {text: 'Two', cols: 2, rows: 8, color: '#142A5C'},

  ];
  ngAfterViewInit(): void {

  }

}
