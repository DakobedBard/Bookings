# Generated by Django 2.2.8 on 2020-03-22 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200322_1835'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='host',
            name='location',
        ),
    ]