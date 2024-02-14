from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import random
from fake_email import Email


class ApiHome(View):
    def get(self, request):
        return render(request, 'appApi/index.html')
    def post(self, request):
        action = request.POST['action']
        if action == 'generate-password':
            data = self.generate_password(request)
        elif action == 'generate-email':
            data = self.generate_email(request)
            
        return JsonResponse(data)
        
    def generate_email(self, request):
        mail=Email().Mail()
        print(mail)
        count_email = request.POST('number_len')
    def generate_password(self, request):
        length_gen = request.POST["gen_length"]
        amount_gen = request.POST["gen_amount"]
        data_chars = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
        data_pwds = []
        for psw in range(int(amount_gen)):
            data_pwds.append("".join(random.sample(data_chars, int(length_gen))))
        return({
                'status' : 'ok',
                'data' : data_pwds
                })