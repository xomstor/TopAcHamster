# Generated by Django 5.0 on 2024-03-18 17:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appResponse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generatedate',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False, verbose_name='Дата и время'),
        ),
        migrations.AlterField(
            model_name='generatedate',
            name='status',
            field=models.BooleanField(blank=True, default=True, help_text='Да (активно) или Нет (неактивно)', null=True, verbose_name='Разрешение'),
        ),
        migrations.AlterField(
            model_name='generatenumber',
            name='number',
            field=models.IntegerField(default=214, verbose_name='Число'),
        ),
    ]
