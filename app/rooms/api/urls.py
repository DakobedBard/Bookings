from django.urls import path
from rooms.api.views import  RoomDetailView, RoomViewSet

urlpatterns = [
    path(r'create_room/', RoomDetailView.as_view(), name='create'),
    path('<int:id>/get/', RoomDetailView.as_view(),  name='getRoom'),
    path(r'list_rooms/', RoomViewSet.as_view({'get': 'list'}), name='detail'),
    path('<int:id>/delete/', RoomDetailView.as_view()),
]
