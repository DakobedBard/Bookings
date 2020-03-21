import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpResponse } from '@angular/common/http';
import { Room } from './room'
import { retry, catchError, tap } from 'rxjs/operators';
import { Observable, of } from 'rxjs';
import { MessageService } from './message.service';

const headers = new HttpHeaders({
  'Content-Type': 'application/json'
});

@Injectable({
  providedIn: 'root'
})
export class RoomService {
  djangoURL: string = 'http://localhost:8000'
  constructor(private  httpClient:HttpClient,private messageService: MessageService) { }
  
  getRooms(){
    return this.httpClient.get(`${this.djangoURL}/rooms/list_rooms`)
  }
  
  getRoom(id: number): Observable<Room> {
    const url = `${this.djangoURL}/rooms/${id}/get`;
    return this.httpClient.get<Room>(url).pipe(
      tap(_ => this.log(`fetched room id=${id}`)),
      catchError(this.handleError<Room>(`getRoom id=${id}`))
    );
  }
  
  postRoom(room){
    return this.httpClient.post(`${this.djangoURL}/rooms/rooms/`,room, {headers:headers}).pipe(
      tap(data => {
        let obj = JSON.parse(JSON.stringify(data));
        localStorage.setItem('currentUserID',JSON.stringify(obj.userid));  
      })
    )
  }

  private handleError<T> (operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {

      // TODO: send the error to remote logging infrastructure
      console.error(error); // log to console instead

      // TODO: better job of transforming error for user consumption
      this.log(`${operation} failed: ${error.message}`);

      // Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }

    /** Log a HeroService message with the MessageService */
  private log(message: string) {
    this.messageService.add(`HeroService: ${message}`);
  }

}
