# Generated by Django 3.1.1 on 2020-11-02 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tinyfunds', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='idnum',
        ),
        migrations.AddField(
            model_name='event',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateTimeField(),
        ),
    ]
