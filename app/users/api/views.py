
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from django.http import HttpResponse
from django.db.models import Q
from .serializers import GuestSerializer, HostSerializer
from users.models import Guest, Host
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

class GuestDetailView(APIView):
    def post(self,request,*args,**kwargs):
        guest_serializer = GuestSerializer(data=request.data)
        if guest_serializer.is_valid():
            guest_serializer.save()
            return Response(guest_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(guest_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id =None):
        try:
            guest = Guest.objects.get(id=id)
            guest.delete()
            return HttpResponse(status=204)
        except Guest.DoesNotExist as e:
            return Response({"error": "Given Tab object not found."}, status=404)

class HostDetailView(APIView):
    def post(self,request,*args,**kwargs):
        host_serializer = HostSerializer(data=request.data)
        if host_serializer.is_valid():
            host_serializer.save()
            return Response(host_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(host_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id =None):
        try:
            guest = Guest.objects.get(id=id)
            guest.delete()
            return HttpResponse(status=204)
        except Guest.DoesNotExist as e:
            return Response({"error": "Given Tab object not found."}, status=404)




class GuestViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request, lat, long, keyword):
        print("The lat is " + lat)
        keywords = keyword
        keywordsplit = keywords.split(',')
        for word in keywordsplit:
            print(word)

        queryset = Guest.objects.all()
        serializer = GuestSerializer(queryset, many=True)
        return Response(serializer.data)

