
from rest_framework.views import APIView

from .serializers import RoomSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response as resp  # This was necessary because it was calling
from rest_framework import status
from rooms.models import Room

class RoomDetailView(APIView):
    def get(self,request,id =None):
        print("I get here!!" + str(id))
        try:
            queryset = Room.objects.filter(id=id)
            serializer = RoomSerializer(queryset, many=True)
            return resp(serializer.data)
        except Room.DoesNotExist as e:
            return resp({"error": "Room not found."}, status=404)

    def post(self,request,*args,**kwargs):
        room_serializer = RoomSerializer(data=request.data)
        if room_serializer.is_valid():
            room_serializer.save()
            return Response(room_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(room_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id =None):
        try:
            tab = Room.objects.get(id=id)
            tab.delete()
            return resp(status=204)
        except Room.DoesNotExist as e:
            return Response({"error": "Given Tab object not found."}, status=404)


from rest_framework import viewsets
from rest_framework.response import Response

class RoomViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = Room.objects.all()
        serializer = RoomSerializer(queryset, many=True)
        return Response(serializer.data)
