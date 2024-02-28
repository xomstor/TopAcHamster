from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import ContentNews


class PageAuth(View):
    def get(self, request):
        # print(request.user.is_authenticated)
        
        # try: 
        #     ContentNews.objects.get(title = 'Хурма внутри')
        # except:
        #     ContentNews.objects.create(
        #         title = 'Хурма внутри',
        #         name_url = 'Хурма внутри',
        #     )
        # вместо этого трайк эксепт можно новым методом
        
        # get_mews, created_news = ContentNews.objects.get_or_create(title = 'Хурма внутри', name_url = 'Хурма внутри')
        # print(get_mews)
        # print(created_news)      
        # print(request.GET.get('last_name', None))  
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
            
class PageReg(View):
    def get(self, request):
        return render(request, 'appAuth/reg/index.html')
    def post(self, request):
        newlogin = request.POST['login']
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        password = request.POST['password']
        status =''
        try:
            User.objects.get(username=newlogin)
            status += 'error'
        except:
            status += 'ok'
            User.objects.create(
                username = newlogin,
                first_name = name,
                last_name = surname,
                email = email,
                password = password
            )
            return JsonResponse({})
