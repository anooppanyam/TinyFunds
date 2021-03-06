# Generated by Django 3.1.1 on 2020-11-09 05:08

from django.db import migrations
import django_google_maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tinyfunds', '0010_remove_event_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='geolocation',
            field=django_google_maps.fields.GeoLocationField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='address',
            field=django_google_maps.fields.AddressField(default='University of Virginia', max_length=200),
        ),
    ]
