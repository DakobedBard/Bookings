import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpResponse } from '@angular/common/http';
@Injectable({
  providedIn: 'root'
})
export class BookingsService {
  djangoURL: string = 'http://localhost:8000/rooms/list_rooms'
  constructor(private  httpClient:HttpClient) { }
  
  getListings() {
    return this.httpClient.get(this.djangoURL);
  }
  

}
