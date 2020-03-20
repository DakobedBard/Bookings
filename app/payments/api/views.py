
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from django.http import HttpResponse
from django.db.models import Q
from .serializers import GuestPaymentSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from payments.models import GuestPaymentInfo

class GuestPaymentDetailView(APIView):
    def post(self,request,*args,**kwargs):
        file_serializer = GuestPaymentSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id =None):
        try:
            tab = GuestPaymentInfo.objects.get(id=id)
            tab.delete()
            return HttpResponse(status=204)
        except GuestPaymentInfo.DoesNotExist as e:
            return Response({"error": "Given Tab object not found."}, status=404)


from rest_framework import viewsets
from rest_framework.response import Response

class GuestPaymentViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request, lat, long, keyword):
        print("The lat is " + lat)
        keywords = keyword
        keywordsplit = keywords.split(',')
        for word in keywordsplit:
            print(word)
        queryset = GuestPaymentInfo.objects.all()
        serializer = GuestPaymentSerializer(queryset, many=True)
        return Response(serializer.data)
