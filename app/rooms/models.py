from django.db import models
from users.models import Host
import datetime
from django.utils.timezone import now
from django.contrib.postgres.fields import JSONField, ArrayField

class Room(models.Model):
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, default="Room1")
    address =  models.CharField(max_length=30, default="8 mile")
    city = models.CharField(max_length=40, default="Detroit")
    state = models.CharField(max_length=30, default="Michigan")
    country = models.CharField(max_length=30, default='UnitedStates')
    lat = models.FloatField(default=-98.0)
    long = models.FloatField(default=40.0)
    property_type = models.CharField(max_length=50, default="1 BR appartment")
    guest_count = models.IntegerField(default=1)
    bed_count = models.IntegerField(default=1)
    bath_count = models.IntegerField(default=1)
    description = models.CharField(max_length=500, default="No description")
    available_date = models.DateField(("Date"), default=datetime.date.today)
    auto_approve = models.BooleanField(default=True)
    price = models.IntegerField(default=300)
    published = models.DateField(("Date"), default=datetime.date.today)
    reserved_dates = ArrayField(JSONField(default=list), null=True)

