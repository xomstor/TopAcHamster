# Generated by Django 5.0 on 2024-03-18 16:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GenerateDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now, editable=False, verbose_name='Дата и время')),
                ('status', models.BooleanField(default=False, help_text='Да (активно) или Нет (неактивно)', verbose_name='Разрешение')),
            ],
            options={
                'verbose_name': 'Дату и время',
                'verbose_name_plural': 'Даты и времена',
            },
        ),
        migrations.CreateModel(
            name='GenerateNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=357, verbose_name='Число')),
                ('status', models.BooleanField(default=True, help_text='Да (активировать) или Нет (деактивировать)', verbose_name='Разрешение')),
            ],
            options={
                'verbose_name': 'Число',
                'verbose_name_plural': 'Числа',
            },
        ),
    ]