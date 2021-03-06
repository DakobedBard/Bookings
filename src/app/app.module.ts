import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { MaterialModule } from './material/material.module'
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { HttpClientModule,HTTP_INTERCEPTORS }    from '@angular/common/http';

import { FormsModule, ReactiveFormsModule }    from '@angular/forms';
import { BookingsSearchComponent } from './bookings-search/bookings-search.component';
import { RoomDetailComponent } from './rooms/room-detail/room-detail.component';
import { PostRoomComponent } from './post-room/post-room.component';
import { ListRoomsComponent } from './rooms/list-rooms/list-rooms.component';
import { RegisterComponent } from './register/register.component';
import { AppRoutingModule }     from './app-routing.module';
import { DashboardComponent } from './dashboard/dashboard.component';
import { LoginComponent } from './login/login.component';


@NgModule({
  declarations: [
    AppComponent,
    BookingsSearchComponent,
    RoomDetailComponent,
    PostRoomComponent,
    ListRoomsComponent,
    RegisterComponent,
    DashboardComponent,
    LoginComponent,
    RoomDetailComponent,
  ],
  imports: [
    BrowserModule,
    MaterialModule,
    BrowserAnimationsModule,
    HttpClientModule,
    ReactiveFormsModule,
    FormsModule,
    AppRoutingModule
  ],
  providers: [],
  exports: [AppRoutingModule],
  bootstrap: [AppComponent]
})
export class AppModule { }
