import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Service } from '../document.service';
import { Document } from '../document';
import { FormBuilder, FormGroup } from '@angular/forms';
import { Router } from '@angular/router'
import { HttpClient,HttpHeaders } from '@angular/common/http';
import { MessageService } from '../message.service'
 
@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: [ './dashboard.component.css' ]
})
export class DashboardComponent implements OnInit {
  tabs: any[];

  createTabMode: boolean = false;
  constructor(){}
    ngOnInit() {
     
      
    }
}
