
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from django.http import HttpResponse
from .serializers import ReserverationSerializer
from rest_framework import status
from reservations.models import Reservation
from rest_framework import viewsets
from rooms.models import Room
from rest_framework.response import Response
from utils.date_utils import date_range_list
from datetime import date, timedelta

class ReservationDetailView(APIView):
    def post(self,request,*args,**kwargs):
        print("YOO" + "dfd")
        reservation_serializer = ReserverationSerializer(data=request.data)
        print("request data " + str(request.data['room']))

        if reservation_serializer.is_valid():
            roomID = request.data['room']
            startDate = reservation_serializer.validated_data['checkin_date']
            endDate = reservation_serializer.validated_data['checkout_date']
            dates = date_range_list(startDate, endDate)

            if len(dates) == 0:
                return Response("Checkout date is before the checkin date", status=status.HTTP_400_BAD_REQUEST)

            room = Room.objects.get(id=roomID)
            print("the rooms name is " + room.name)
            reservation_serializer.save()
            return Response(reservation_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(reservation_serializer.error_messages)
            return Response(reservation_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id =None):
        try:
            tab = Reservation.objects.get(id=id)
            tab.delete()
            return HttpResponse(status=204)
        except Reservation.DoesNotExist as e:
            return Response({"error": "Given Tab object not found."}, status=404)

class ReservationViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = Reservation.objects.all()
        print("There are " + str(len(queryset)) + " Rooms available")

        serializer = ReserverationSerializer(queryset, many=True)
        return Response(serializer.data)
