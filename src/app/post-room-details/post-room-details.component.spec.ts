import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PostRoomDetailsComponent } from './post-room-details.component';

describe('PostRoomDetailsComponent', () => {
  let component: PostRoomDetailsComponent;
  let fixture: ComponentFixture<PostRoomDetailsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PostRoomDetailsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PostRoomDetailsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
