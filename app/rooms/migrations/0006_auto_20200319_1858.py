# Generated by Django 2.2.8 on 2020-03-19 18:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_auto_20200319_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='available_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='published',
            field=models.DateField(default=datetime.datetime(2020, 3, 19, 18, 58, 20, 592673)),
        ),
    ]
