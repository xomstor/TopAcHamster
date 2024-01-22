from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class HomePage(View):
    def get(self, request):
        data = {
            'block_css' : "home"
            }
        return render(request, 'Alast/home/index.html', data)
    
