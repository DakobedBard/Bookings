from django.urls import path
from reservations.api.views import  ReservationDetailView, ReservationViewSet

urlpatterns = [
    path(r'book/', ReservationDetailView.as_view(), name='book'),
    path(r'search/', ReservationViewSet.as_view({'get': 'list'}), name='search'),
]