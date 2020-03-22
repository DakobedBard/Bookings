# Generated by Django 2.2.8 on 2020-03-22 00:06

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0008_auto_20200319_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='reserved_dates',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.jsonb.JSONField(default=list), null=True, size=None),
        ),
    ]
