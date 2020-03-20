import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BookingsSearchComponent } from './bookings-search.component';

describe('BookingsSearchComponent', () => {
  let component: BookingsSearchComponent;
  let fixture: ComponentFixture<BookingsSearchComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BookingsSearchComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BookingsSearchComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
