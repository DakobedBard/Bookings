from django.urls import path
from rooms.api.views import  RoomDetailView, RoomViewSet

urlpatterns = [
    path(r'create_room/', RoomDetailView.as_view(), name='detail'),
    path(r'list_rooms/', RoomViewSet.as_view({'get': 'list'}), name='detail'),

]
