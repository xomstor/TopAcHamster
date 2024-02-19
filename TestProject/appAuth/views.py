from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

class PageAuth(View):
    def get(self, request):
        return render(request, 'appAuth/auth/index.html')