# Generated by Django 5.0 on 2023-12-27 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hamsterapp', '0002_alter_formuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formuser',
            name='email',
            field=models.EmailField(db_index=True, help_text='Введіть вашу пошту', max_length=254, unique=True, verbose_name='Пошта'),
        ),
    ]
