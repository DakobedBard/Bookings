import { Component, OnInit } from '@angular/core';
import { FormGroup,ReactiveFormsModule, FormBuilder,FormArray, Validators, FormControl,NgForm  } from '@angular/forms';
import { BookingsService } from '../bookings.service';

@Component({
  selector: 'app-bookings-search',
  templateUrl: './bookings-search.component.html',
  styleUrls: ['./bookings-search.component.css']
})
export class BookingsSearchComponent implements OnInit {
  searchForm: FormGroup;
  constructor(private formBuilder: FormBuilder,private bookingServie: BookingsService) { }

  startDate: Date;
  endDate: Date;

  ngOnInit() {
    this.searchForm  =  this.formBuilder.group({
      location: ['', Validators.required],
    });
  }

  searchFor() {
    var start_date = this.startDate.toString()
    var end_date = this.endDate.toString()
    var location = this.searchForm.value.location

    console.log("And the location is " + location)
    console.log("Start date " + start_date)
    console.log("End date " + end_date)
  }    
}
