# Generated by Django 3.1.1 on 2020-11-09 16:15

from django.db import migrations
import places.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tinyfunds', '0013_auto_20201109_0538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='location',
            field=places.fields.PlacesField(max_length=255),
        ),
    ]
