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
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        FormUser.objects.create(name=name,
                                email=email,
                                age=age)
        # request.session['name'] = name
        # request.session['email'] = email
        # request.session['age'] = age
        return redirect('index')