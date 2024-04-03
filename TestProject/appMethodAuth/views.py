from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User as User


class AuthPage(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('url-account')
        return render(request, 'appMethodAuth/auth.html')
    def post(self, request):
        login = request.POST['login']
        password = request.POST['password']
        user = authenticate(
            request,
            username=login,
            password=password
        )
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('url-account')
            return HttpResponse('Пользователь не активен')    
        return HttpResponse('Неверный логин или пароль')

class AccountPage(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('url-methodauth')
        return render(request, 'appMethodAuth/account.html')
    
class LogoutPage(View):
    def get(self, request):
        logout(request)
        return redirect('url-methodauth')

class RegPage(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('url-account')
        return render(request, 'appMethodAuth/reg.html')
    def post(self, request):
        name = request.POST['name']
        user = User.objects.filter(username=name)
        email = request.POST['email']
        login = request.POST['login']
        password = request.POST['password']
        if not user.exists():
            User.objects.create(
                username = login,
                first_name = name,
                email = email,
                password = make_password(password)
            )
            return redirect('url-methodauth')
        return HttpResponse('Пользователь с таким именем уже существует')
    