# Generated by Django 3.1.1 on 2020-11-08 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tinyfunds', '0005_event_owner_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='address',
            field=models.CharField(max_length=1024, null=True),
        ),
    ]
