# Generated by Django 5.0 on 2024-03-04 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PubNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Содержание')),
                ('date_time', models.DateTimeField(auto_now_add=True, verbose_name='дата и время публикации')),
                ('url_name', models.CharField(max_length=25, verbose_name='url, имя ссылки')),
            ],
            options={
                'verbose_name': 'Публикация',
                'verbose_name_plural': 'Публикации',
            },
        ),
    ]
