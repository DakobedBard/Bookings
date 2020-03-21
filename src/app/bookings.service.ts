import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpResponse } from '@angular/common/http';
import { retry, catchError, tap } from 'rxjs/operators';
import { Reservation } from './reservation'

const headers = new HttpHeaders({
  'Content-Type': 'application/json'
});

@Injectable({
  providedIn: 'root'
})

export class BookingsService {
  djangoURL: string = 'http://localhost:8000/reservations'
  constructor(private  httpClient:HttpClient) { }
  
  bookRoom(reservation: Reservation){
    return this.httpClient.post(`${this.djangoURL}/book/`, reservation, {headers:headers}).pipe(
      tap(data => {
        let obj = JSON.parse(JSON.stringify(data));
        localStorage.setItem('currentUserID',JSON.stringify(obj.userid));  
      })
    )
  }
}
