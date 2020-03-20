from django.urls import path
from reservations.api.views import  ReservationDetailView, ReservationViewSet

urlpatterns = [
    path(r'book_reservation/', ReservationDetailView.as_view(), name='detail'),
    path(r'search_reservations/', ReservationViewSet.as_view({'get': 'list'}), name='search'),
]