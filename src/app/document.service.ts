import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Observable, of } from 'rxjs';
import { catchError, map, tap } from 'rxjs/operators';

import { Document } from './document';
import { MessageService } from './message.service';


@Injectable({ providedIn: 'root' })
export class Service {

  private documentsUrl = 'http://localhost:8000/upload/';
  documents: any = [];
  httpOptions:any = { 
    headers: new HttpHeaders({
      'Content-Type': 'multipart/form-data'
    }),
  }; 

  constructor(
    private http: HttpClient,
    private messageService: MessageService) { }

  /** GET documents from the server */

  getDocuments(id: any) {
    console.log("id " + id)
    return this.http.get(this.documentsUrl+'/list/'+id);
    // return this.http.get(this.documentsUrl+'?id=1');
  }
  createDocument(document) {
    return this.http.post(this.documentsUrl+'/upload/',document,this.httpOptions);
  }

  /**
   * Handle Http operation that failed.
   * Let the app continue.
   * @param operation - name of the operation that failed
   * @param result - optional value to return as the observable result
   */
  private handleError<T> (operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {

      // TODO: send the error to remote logging infrastructure
      console.error(error); // log to console instead

      // TODO: better job of transforming error for user consumption
      

      // Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }

}
