# Generated by Django 3.1.1 on 2020-11-02 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tinyfunds', '0004_auto_20201102_1916'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='owner_id',
            field=models.IntegerField(default=1),
        ),
    ]
