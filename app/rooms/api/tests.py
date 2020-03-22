import json
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status


class RoomTestCase(APITestCase):

    def test_create_room(self):
        response = self.client.post(
            path='http://127.0.0.1:8000/rooms/create_room/',
            data=json.dumps({
                'host':1
            }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        #, 'state':'Arkansas','city':'bonerville'}
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)