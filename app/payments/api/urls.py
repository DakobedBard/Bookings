from django.urls import path
from payments.api.views import  GuestPaymentDetailView, GuestPaymentViewSet

urlpatterns = [

    path('tweet/<lat>/<long>/<keyword>/', GuestPaymentViewSet.as_view({'get': 'list'})),
    path(r'detail/', GuestPaymentDetailView.as_view(), name='detail'),
]