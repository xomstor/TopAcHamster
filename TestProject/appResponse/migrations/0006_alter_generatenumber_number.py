# Generated by Django 5.0.3 on 2024-03-20 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appResponse', '0005_alter_generatenumber_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generatenumber',
            name='number',
            field=models.IntegerField(default=123, verbose_name='Число'),
        ),
    ]