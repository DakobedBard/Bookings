from django.urls import path
from users.api.views import GuestDetailView, GuestViewSet, HostDetailView

urlpatterns = [
    path('guest_create/', GuestViewSet.as_view({'get': 'list'})),
    path('create_guest/', GuestDetailView.as_view(), name='guest'),
    path('create_host/', HostDetailView.as_view(), name='host'),
]