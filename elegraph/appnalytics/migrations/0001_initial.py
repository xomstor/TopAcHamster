# Generated by Django 5.0 on 2024-03-06 18:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appPublication', '0004_delete_articles_alter_pubnews_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableOfUserAgents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_agent', models.TextField(blank=True, null=True, verbose_name='Пользовательский агент')),
                ('user_agent_parse_os', models.TextField(blank=True, null=True, verbose_name='user_agent_parse_os')),
                ('user_agent_parse_browser', models.TextField(blank=True, null=True, verbose_name='user_agent_parse_browser')),
                ('user_agent_parse_is_bot', models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No'), (None, 'ХЗ')], default=False, null=True, verbose_name='bot?')),
                ('user_agent_parse_is_touch', models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No'), (None, 'ХЗ')], default=False, null=True, verbose_name='тачевое?')),
                ('device_type', models.CharField(blank=True, choices=[('mobile', 'mobile'), ('tablet', 'tablet'), ('desktop', 'PC')], max_length=100, null=True, verbose_name='device_type')),
                ('pub_news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPublication.pubnews', verbose_name='Публикация')),
            ],
            options={
                'verbose_name': 'История (статистика) Пользовательский агент',
                'verbose_name_plural': 'Просмотры (статистика) Пользовательские агенты',
            },
        ),
    ]
