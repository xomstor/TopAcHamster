# Generated by Django 5.0 on 2024-03-18 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appResponse', '0003_alter_generatenumber_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generatenumber',
            name='number',
            field=models.IntegerField(default=297, verbose_name='Число'),
        ),
    ]
