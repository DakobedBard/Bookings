
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from django.http import HttpResponse
from .serializers import ReserverationSerializer
from rest_framework import status
from reservations.models import Reservation
from rest_framework import viewsets
from rest_framework.response import Response

class ReservationDetailView(APIView):
    def post(self,request,*args,**kwargs):
        print("YOO")
        file_serializer = ReserverationSerializer(data=request.data)
        print("request data " + str(request.data))

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(file_serializer.error_messages)
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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
