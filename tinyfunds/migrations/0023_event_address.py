# Generated by Django 3.1.1 on 2020-11-09 21:03

from django.db import migrations
import places.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tinyfunds', '0022_remove_event_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='address',
            field=places.fields.PlacesField(blank=True, max_length=255),
        ),
    ]
