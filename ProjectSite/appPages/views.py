from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import ContentBanner, AboutMe
class HomePage(View):
    def get(self, request):
        data = {
            'banner':ContentBanner.objects.order_by("number"),
        }
        return render(request, 'appPages/home/index.html', data)
    
class AboutMePage(View):
    def get(self, request):
        data = {
            'about':AboutMe.objects.all(),
        }
        return render(request, 'appPages/about/index.html', data)