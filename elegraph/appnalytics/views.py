from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import TableOfUserAgents
from collections import Counter

class UALinkPage(View):
    def get(self, request, name_link):
        staticsobj = TableOfUserAgents.objects.filter(
            pub_news__url_name=name_link
        )
        object_browser = dict(Counter(staticsobj.values_list('user_agent_parse_browser', flat=True)))
        object_tablet_or_pc = dict(Counter(staticsobj.values_list('device_type', flat=True)))
        print(object_tablet_or_pc), print(object_browser)
        object_os = dict(Counter(staticsobj.values_list('user_agent_parse_os', flat=True)))
        object_is_bot = dict(Counter(staticsobj.values_list('user_agent_parse_is_bot', flat=True)))
        return render(
            request, 
            'appnalytics/base.html',
            {
                "browsers" : object_browser,
                "os" : object_os,
                "tablet_or_pc" : object_tablet_or_pc,
                "is_bot" : object_is_bot
            }
        )
        # return HttpResponse('Главная статистика пользователя')