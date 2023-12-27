from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

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
        print(request.POST)
        print(request.POST['number'])
        return HttpResponse("Hello, world. You're at the Hamsterapp index.")