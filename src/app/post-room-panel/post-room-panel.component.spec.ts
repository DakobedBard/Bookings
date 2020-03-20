import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PostRoomPanelComponent } from './post-room-panel.component';

describe('PostRoomPanelComponent', () => {
  let component: PostRoomPanelComponent;
  let fixture: ComponentFixture<PostRoomPanelComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PostRoomPanelComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PostRoomPanelComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
