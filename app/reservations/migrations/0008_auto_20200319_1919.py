# Generated by Django 2.2.8 on 2020-03-19 19:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0007_auto_20200319_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='billing_address',
            field=models.CharField(default='35th AVE NE', max_length=150),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='card_no',
            field=models.CharField(default='8400611124561232', max_length=20),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='checkin_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='checkout_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]
