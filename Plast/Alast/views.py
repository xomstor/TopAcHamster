from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class HomePage(View):
    def get(self, request):
        return render(request, 'Alast/home/index.html')
    
class NewsPage(View):
    def get(self, request):
        return render(request, 'Alast/news/index.html')
    
class OfferPage(View):
    def get(self, request):
        return render(request, 'Alast/offer/index.html')
    