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
    location = models.CharField(max_length=30, default="Nebrasa")
    first_name = models.CharField(max_length=30, default="Joseph")
    last_name = models.CharField(max_length=30, default="Dulapp")
    email = models.CharField(max_length=30, default="Nebrasa")
    phone_number = models.CharField(max_length=15, default=" ")
    address = models.CharField(max_length=60, default='8009 39th AVE NE')
    city = models.CharField(max_length=30, default='Seattle')
    state = models.CharField(max_length=30, default='Washington')
    country = models.CharField(max_length=30, default='United States')
    zip = models.IntegerField( default=98115)



guest_table_create = (""" CREATE TABLE IF NOT EXISTS guests(
                            guest_id serial PRIMARY KEY ,
                            name CHAR NOT NULL,
                            email CHAR NOT NULL,
                            phone CHAR NOT NULL,
                            username CHAR NOT NULL,
                            password CHAR NOT NULL,
                            address CHAR NOT NULL,
                            city CHAR NOT NULL,
                            state CHAR NOT NULL,
                            country CHAR NOT NULL,
                            zip INT NOT NULL
                        );""")

host_table_create = (""" CREATE TABLE IF NOT EXISTS hosts(
                            host_id serial PRIMARY KEY ,
                            name CHAR NOT NULL,
                            email CHAR NOT NULL,
                            phone CHAR NOT NULL,
                            username CHAR NOT NULL,
                            password CHAR NOT NULL,
                            address CHAR NOT NULL,
                            city CHAR NOT NULL,
                            state CHAR NOT NULL,
                            country CHAR NOT NULL,
                            zip INT NOT NULL);
                        """)
