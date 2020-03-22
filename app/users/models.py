from django.db import models

class Guest(models.Model):
    first_name = models.CharField(max_length=30, default="Joseph")
    last_name = models.CharField(max_length=30, default="Dulapp")
    email = models.CharField(max_length=30, default="")
    phone_number = models.CharField(max_length=15, default=" ")
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    address = models.CharField(max_length=60, default='8009 39th AVE NE')
    city = models.CharField(max_length=30, default='Seattle')
    state = models.CharField(max_length=30, default='Washington')
    country = models.CharField(max_length=30, default='United States')
    zip = models.IntegerField( default=98115)

class Host(models.Model):
    username = models.CharField(max_length=30, default="firstTab.txt")
    password = models.CharField(max_length=30, default = "pass123")
    first_name = models.CharField(max_length=30, default="Joseph")
    last_name = models.CharField(max_length=30, default="Dulapp")
    email = models.CharField(max_length=30, default="Nebrasa")
    phone_number = models.CharField(max_length=35, default=" ")
    address = models.CharField(max_length=60, default='8009 39th AVE NE')
    city = models.CharField(max_length=30, default='Seattle')
    state = models.CharField(max_length=30, default='Washington')
    country = models.CharField(max_length=30, default='United States')
    zip = models.IntegerField( default=98115)
