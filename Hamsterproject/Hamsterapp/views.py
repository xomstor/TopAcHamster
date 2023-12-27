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
        method = request.POST.get('method')
        if method == 'update':
            try:
                FormUser.objects.filter(email=user_email).update(
                name=user_name
                )
            except:
                pass
        elif method == 'update_age':
            user_age = request.POST.get('age')
            try:
                if user_name == '':
                    FormUser.objects.filter(email=user_email).update(
                    age=user_age
                    )
                else:
                    FormUser.objects.filter(name=user_name).update(
                    age=user_age
                    )
            except:
                pass
        elif method == 'create':
            try:
                FormUser.objects.create(
                name=user_name,
                email=user_email
                )
            except:
                pass

        # request.session['name'] = name
        # request.session['email'] = email
        # request.session['age'] = age
        return redirect('index')
    