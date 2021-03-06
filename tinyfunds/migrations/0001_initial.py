# Generated by Django 3.1.1 on 2020-11-02 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('idnum', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('org_name', models.CharField(blank=True, max_length=254, null=True)),
                ('description', models.CharField(blank=True, max_length=254, null=True)),
                ('pic', models.CharField(default='https://avatars2.githubusercontent.com/u/3195011?s=460&u=f421eadccb78b212d516b6b38cab7f2de97522e4&v=4', max_length=1024)),
                ('event_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
