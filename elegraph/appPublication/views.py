from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views import View
import uuid
from .models import PubNews
from user_agents import parse

class PublicationPage(View):
    def get(self, request):
        return render(request, 'appPublication/views-edit.html')
    def post(self, request):
        print(request.POST)
        name_url = str(uuid.uuid4())[:5]
        get_pub, created = PubNews.objects.get_or_create(
            url_name = name_url,
            defaults={
                'content' : request.POST['content']
            })
        if created:
            return JsonResponse({
            'status' : 'ok',
            'url' : get_pub.url_name
            })
        # if created:
        #     get_pub.content = request.POST['content']
        #     get_pub.save()
        return JsonResponse({
            'status' : 'error'
        })

class OpenPublicPage(View):
    def get(self, request, url_name_pub):
        user_agent = request.META['HTTP_USER_AGENT']
        ua_parse = parse(user_agent)
        print(ua_parse.os)
        print(ua_parse.browser)
        print(ua_parse.device)
        print(ua_parse.is_bot)        
        print(ua_parse.is_mobile)
        print(ua_parse.is_tablet)
        print(ua_parse.is_email_client)
        print(user_agent)
        try:
            obj_pub = PubNews.objects.get(url_name = url_name_pub)
            return render(request, 'appPublication/result.html', {'content_obj' : obj_pub.content})
        except:
            return redirect('url-open-publication')
        
        