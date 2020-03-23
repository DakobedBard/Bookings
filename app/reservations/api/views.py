from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from django.http import HttpResponse
from reservations.api.serializers import ReserverationSerializer
from rest_framework import status
from reservations.models import Reservation
from rest_framework import viewsets

from rest_framework.response import Response
from utils.date_utils import date_range_list
from datetime import date, timedelta
from rooms.models import Room


'''
This could and should be moved to a method on the Room model
'''

def add_dates(room, dates):

    [room.reserved_dates.append(str(day)) for day in dates]
    room.save()

def remove_dates(roomID, checkInDate, checkOutDate):
    room = Room.objects.get(id=roomID)
    dates = date_range_list(checkInDate, checkOutDate)
    [room.reserved_dates.remove(str(day)) for day in dates]
    room.save()

def validate_dates(room, dates):
    reserved_dates = room.reserved_dates
    print("reserveed dates " + str(reserved_dates))
    print("Incoming dates " + str(dates))
    for date in dates:
        if str(date) in reserved_dates:
            return False
    # print("Validation is not working!")
    return True

class ReservationDetailView(APIView):

    def post(self,request,*args,**kwargs):
        reservation_serializer = ReserverationSerializer(data=request.data)
        if reservation_serializer.is_valid():
            roomID = request.data['room']
            room = Room.objects.get(id=roomID)

            startDate = reservation_serializer.validated_data['checkin_date']
            endDate = reservation_serializer.validated_data['checkout_date']

            dates = date_range_list(startDate, endDate)
            print("The type of room is " + str(type(room)))

            if len(dates) == 0:
                return Response("Invalid date selection", status=status.HTTP_400_BAD_REQUEST)
            if not validate_dates(room, dates):
                return Response("Invalid date selection", status=status.HTTP_409_CONFLICT)

            add_dates(room, dates)
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
