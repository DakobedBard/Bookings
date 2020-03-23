from users.models import Guest
from rooms.models import Room
from django.db import models
import datetime
from django.utils.timezone import now
from enum import Enum

class ReservationStatus(str, Enum):
    '''
    First time experimenting with an Enum value in a Django model.   If I do not inherit from 'str' then I will have
    serialization problems.
    '''

    pending = "Pending"
    reserved = "Reserved"
    cancelled = "Cancelled"
    awaiting = "Awaiting"

class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, default=1)
    checkin_date = models.DateField(("Date"), default=datetime.date.today)
    checkout_date = models.DateField(("Date"), default=datetime.date.today)
    guest_count = models.IntegerField(default=1)
    price = models.IntegerField(default=200)
    status = models.CharField(max_length=15, default="Vacant")
    billing_address = models.CharField(max_length=150, default='35th AVE NE')
    city = models.CharField(max_length=200, default='Detroit')
    state = models.CharField(max_length=20, default='Michigan')
    country = models.CharField(max_length=30, default='United States')
    card_no = models.CharField(max_length=20, default='8400611124561232')
    active = models.BooleanField(default=False)

    # status = models.CharField(max_length=30,
    #                           choices=[(tag, tag.value) for tag in ReservationStatus],
    #                           default=ReservationStatus.awaiting)