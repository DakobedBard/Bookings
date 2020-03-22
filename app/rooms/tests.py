import json
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status


class RoomTestCase(APITestCase):

    def test_create_room(self):
        pass