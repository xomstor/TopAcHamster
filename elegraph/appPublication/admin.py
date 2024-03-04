from django.contrib import admin
from .models import PubNews


class PubNewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'date_time', 'url_name')
    list_display_links = ('url_name', 'date_time')
    ordering = ('-date_time',)

admin.site.register(PubNews, PubNewsAdmin)

