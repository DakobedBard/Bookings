# Generated by Django 2.2.8 on 2020-03-23 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200322_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='email',
            field=models.CharField(default='Nebrasa', max_length=30),
        ),
        migrations.AlterField(
            model_name='guest',
            name='password',
            field=models.CharField(default='iksarman', max_length=30),
        ),
        migrations.AlterField(
            model_name='guest',
            name='phone_number',
            field=models.CharField(default=' ', max_length=35),
        ),
        migrations.AlterField(
            model_name='guest',
            name='username',
            field=models.CharField(default='user1', max_length=30),
        ),
    ]
