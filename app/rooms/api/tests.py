import json
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from rooms.models import Room
from utils.test_utils.date_seeder import DataSeeder

class RoomTestCase(APITestCase):
    def setUp(self) -> None:
        DataSeeder.seed_host('utils/test_utils/host_directory.csv')

    def test_create_room(self):
        response = self.client.post(
            path="http://127.0.0.1:8000/rooms/create_room/",
            data=json.dumps({
                "host":1,
                'state': 'Arkansas',
                'city': 'bonerville'
            }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        roomID = 1
        room = Room.objects.get(id=roomID)
        response = self.client.post(
            path="http://127.0.0.1:8000/rooms/%d/delete" % roomID,
            data=json.dumps({
                "host":1,
                'state': 'Arkansas',
                'city': 'bonerville'
            }),
            content_type='application/json'
        )

        # print("Response data " + response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_remove_room(self):
        pass
        # response = self.client.post(
        #     path="http://127.0.0.1:8000/rooms/create_room/",
        #     data=json.dumps({
        #         "host":1,
        #         'state': 'Arkansas',
        #         'city': 'bonerville'
        #     }),
        #     content_type='application/json'
        # )
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # #
        # roomID = 1
        # room = Room.objects.get(id=roomID)
        # response = self.client.post(
        #     path="http://127.0.0.1:8000/rooms/%d/delete" % roomID,
        #     data=json.dumps({
        #         "host":1,
        #         'state': 'Arkansas',
        #         'city': 'bonerville'
        #     }),
        #     content_type='application/json'
        # )
        #
        # print("Response data " + response.data)
        # # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #
