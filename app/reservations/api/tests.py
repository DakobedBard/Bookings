import json
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from rooms.models import Room
from users.models import Host, Guest
from utils.test_utils.date_seeder import DataSeeder
from django.db.models import  Min

class RoomTestCase(APITestCase):
    def setUp(self) -> None:
        DataSeeder.default_seed()
        # DataSeeder.seed_data('host','hosts.csv')


    def test_book_reservation(self):
        # The first guest in the database will make a booking
        guestID = Guest.objects.all().aggregate(Min('id'))['id__min'] #
        roomID = Room.objects.all().aggregate(Min('id'))['id__min']  #

        booking_create_response = self.client.post(
            path="http://127.0.0.1:8000/reservations/book/",
            data=json.dumps({
                "room":roomID,
                "guest":guestID,
                'checkin_date':'2020-04-15',
                'checkout_date': '2020-04-18'
            }),
            content_type='application/json'
        )
        self.assertEqual(booking_create_response.status_code, status.HTTP_201_CREATED)

        # Assert that the dates were appeneded to the list
        room = Room.objects.get(id=roomID)
        self.assertEqual(len(room.reserved_dates), 4)


    def test_book_reservation_reserved_dates(self):
        # The first guest in the database will make a booking
        guest1_ID = Guest.objects.all().aggregate(Min('id'))['id__min'] #
        roomID = Room.objects.all().aggregate(Min('id'))['id__min']  #

        booking_create_response = self.client.post(
            path="http://127.0.0.1:8000/reservations/book/",
            data=json.dumps({
                "room":roomID,
                "guest":guest1_ID,
                'checkin_date':'2020-04-15',
                'checkout_date': '2020-04-18'
            }),
            content_type='application/json'
        )
        self.assertEqual(booking_create_response.status_code, status.HTTP_201_CREATED)

        # Assert that the dates were appeneded to the list
        room = Room.objects.get(id=roomID)
        self.assertEqual(len(room.reserved_dates), 4)

        guest2_ID = Guest.objects.all().aggregate(Min('id'))['id__min'] + 1

        booking_create_response = self.client.post(
            path="http://127.0.0.1:8000/reservations/book/",
            data=json.dumps({
                "room":roomID,
                "guest":guest2_ID,
                'checkin_date':'2020-04-17',
                'checkout_date': '2020-04-19'
            }),
            content_type='application/json'
        )
        self.assertEqual(booking_create_response.status_code, status.HTTP_409_CONFLICT)
