# Generated by Django 2.2.8 on 2020-03-19 18:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0003_auto_20200319_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='checkin_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 19, 18, 56, 50, 235803, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='checkout_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 19, 18, 56, 50, 235823, tzinfo=utc)),
        ),
    ]
