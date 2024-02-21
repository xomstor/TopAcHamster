from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.contrib.auth import authenticate, login

class PageAuth(View):
    def get(self, request):
        print(request.user.is_authenticated)
        return render(request, 'appAuth/auth/index.html')
    def post(self, request):
        _login = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request,
            username=login,
            password=password
                            )
        if user is not None:
            if user.is_active:
                login(request, user)
            return JsonResponse({
                'status' : 'ok'
            })
        else:
            return JsonResponse({
                'status' : 'errorNotUser'
            })