# Generated by Django 4.2.7 on 2023-12-03 12:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0012_mailing_owner_serviceclient_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 3, 12, 57, 9, 517325, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 3, 12, 57, 9, 517313, tzinfo=datetime.timezone.utc)),
        ),
    ]