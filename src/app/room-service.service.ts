import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpResponse } from '@angular/common/http';
import { Room } from './room'
import { retry, catchError, tap } from 'rxjs/operators';

const headers = new HttpHeaders({
  'Content-Type': 'application/json'
});

@Injectable({
  providedIn: 'root'
})
export class RoomServiceService {

  djangoURL: string = 'http://localhost:8000'
  constructor(private  httpClient:HttpClient) { }
  // `${this.loginURL}/?username=${user.username}`
  private generateURL(room: Room){
    var hostID = 1;
    return `${this.djangoURL}/rooms/create_room/`
  }


  public postRoom(room){
    var postURL = this.generateURL(room)
    return this.httpClient.post(postURL,room, {headers:headers}).pipe(
      tap(data => {
        let obj = JSON.parse(JSON.stringify(data));
        localStorage.setItem('currentUserID',JSON.stringify(obj.userid));  
      })
    )
  }
}
