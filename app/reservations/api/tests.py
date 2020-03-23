import json
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from rooms.models import Room
from users.models import Host, Guest
from utils.test_utils.date_seeder import DataSeeder

class RoomTestCase(APITestCase):
    def setUp(self) -> None:
        DataSeeder.default_seed()
        # DataSeeder.seed_data('host','hosts.csv')


    def test_book_reservation(self):
        hosts = list(Host.objects.all())
        print("There are " + str(len(hosts)) + " hosts in the DB")
        guests = list(Guest.objects.all())
        print("There are " + str(len(guests)) + " guests in the DB")
        rooms = list(Room.objects.all())
        print("There are " + str(len(rooms)) + " rooms in the DB")
        # host_create_response = self.client.post(
        #     path="http://127.0.0.1:8000/users/create_host/",
        #     data=json.dumps({
        #         "username":"BennyAb",
        #         "password":'iksarman',
        #         'phone_number':'206-321-2211',
        #         'state':'Michigan',
        #         'city': 'Ann Arbor',
        #         'address': '38 Oak street'
        #     }),
        #     content_type='application/json'
        # )
        # self.assertEqual(host_create_response.status_code, status.HTTP_201_CREATED)
