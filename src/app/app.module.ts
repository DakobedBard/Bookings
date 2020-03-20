import { NgModule }       from '@angular/core';
import { BrowserModule }  from '@angular/platform-browser';
import { FormsModule, ReactiveFormsModule }    from '@angular/forms';
import { HttpClientModule,HTTP_INTERCEPTORS }    from '@angular/common/http';

import { AppRoutingModule }     from './app-routing.module';

import { AppComponent }         from './app.component';
import { DashboardComponent }   from './dashboard/dashboard.component';

import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {MaterialModule} from './material/material.module';
import { LoginComponent } from './login/login.component';

import { RegisterComponent } from './register/register.component'
import { TokenInterceptorService } from './token-interceptor.service';
import { BookingsSearchComponent } from './bookings-search/bookings-search.component';
import { RoomDetailComponent } from './room-detail/room-detail.component';
import { PostRoomComponent } from './post-room/post-room.component';
import { PostRoomPanelComponent } from './post-room-panel/post-room-panel.component';
import { PostRoomDetailsComponent } from './post-room-details/post-room-details.component';
import { ListRoomsComponent } from './list-rooms/list-rooms.component';


@NgModule({
  imports: [
    BrowserModule,
    FormsModule,
    AppRoutingModule,
    HttpClientModule,
    BrowserAnimationsModule,  
    MaterialModule,
    ReactiveFormsModule,
    BrowserAnimationsModule,
  ],
  declarations: [
    AppComponent,
    DashboardComponent,
    LoginComponent,
    RegisterComponent,
    // BookingsSearchComponent, 
    // RoomDetailComponent,
    // PostRoomComponent,
    // PostRoomPanelComponent,
    // PostRoomDetailsComponent,
    // ListRoomsComponent 
  ],
  providers: [{
    provide: HTTP_INTERCEPTORS,
    useClass: TokenInterceptorService,
    multi: true,
    
  }],
  bootstrap: [ AppComponent ]
})

export class AppModule { }
