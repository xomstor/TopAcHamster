# Generated by Django 5.0 on 2024-03-11 16:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appnalytics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tableofuseragents',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='дата и время публикации'),
        ),
    ]