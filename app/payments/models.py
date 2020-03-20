from users.models import Host, Guest
from django.db import models

class GuestPaymentInfo(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    billing_address = models.CharField(max_length=150)
    city = models.CharField(max_length=200, default='Detroit')
    state = models.CharField(max_length=20, default='Michigan')
    country = models.CharField(max_length=30, default='United States')
    card_no = models.CharField(max_length=20)
    active = models.BooleanField(default=False)

class HostPaymentInfo(models.Model):
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    billing_address = models.CharField(max_length=150)
    city = models.CharField(max_length=200, default='Detroit')
    state = models.CharField(max_length=20, default='Michigan')

    create_guest_payment_info_table = (""" CREATE TABLE IF NOT EXISTS guest_payment(
                                payment_info_id SERIAL PRIMARY KEY,
                                guest_id INT REFERENCES guests(guest_id) ,
                                billingaddress CHAR NOT NULL,
                                city CHAR NOT NULL,
                                state CHAR NOT NULL,
                                country CHAR NOT NULL,
                                cardinfo CHAR NOT NULL,
                                active BOOL NOT NULL);
                            """)

    create_host_payment_info_table = (""" CREATE TABLE IF NOT EXISTS host_payment_info(
                                payment_info_id SERIAL PRIMARY KEY,
                                host_id INT REFERENCES hosts(host_id) ,
                                billingaddress CHAR NOT NULL,
                                payment_method CHAR NOT NULL,
                                payment_details CHAR NOT NULL,
                                settlement CHAR NOT NULL);
                            """)

