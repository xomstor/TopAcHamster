from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .models import FormUser

class Hamsterhome(View):
    template_home = 'Hamsterapp/index.html'
    def get(self, request):
        ses = request.session.get('hist', False)
        # if ses:
        #     request.session['hist'] = ses + 1
        #     return HttpResponse("Вы вошли на сайт {} раз.".format(ses))
        # else:
        #     request.session['hist'] = 1
        #     return HttpResponse("Вы первыми вошли на сайт!")
        return render(request, self.template_home)
    def post(self, request):
        user_name = request.POST.get('name')
        user_email = request.POST.get('email')
        user_age = request.POST.get('age')
        FormUser.objects.create(name=user_name,
                                email=user_email,
                                age=user_age)
        # request.session['name'] = name
        # request.session['email'] = email
        # request.session['age'] = age
        return redirect('index')