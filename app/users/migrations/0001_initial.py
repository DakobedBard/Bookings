# Generated by Django 2.2.8 on 2020-03-19 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='firstTab.txt', max_length=30)),
                ('email', models.CharField(default='Nebrasa', max_length=30)),
                ('phone_number', models.CharField(default=' ', max_length=15)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('address', models.CharField(default='8009 39th AVE NE', max_length=60)),
                ('city', models.CharField(default='Seattle', max_length=30)),
                ('state', models.CharField(default='Washington', max_length=30)),
                ('country', models.CharField(default='United States', max_length=30)),
                ('zip', models.IntegerField(default=98115)),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='firstTab.txt', max_length=30)),
                ('location', models.CharField(default='Nebrasa', max_length=30)),
            ],
        ),
    ]