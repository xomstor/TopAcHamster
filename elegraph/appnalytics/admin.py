from django.contrib import admin
from .models import TableOfUserAgents

class TableOfUserAgentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'pub_news', 'user_agent', 'user_agent_parse_os', 'user_agent_parse_browser', 'user_agent_parse_is_bot', 'user_agent_parse_is_touch', 'device_type')
    list_display_links = ('pub_news', 'user_agent')
    search_fields = ('pub_news', 'user_agent')
    ordering = ('-pub_news',)

admin.site.register(TableOfUserAgents, TableOfUserAgentsAdmin)
