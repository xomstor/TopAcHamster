from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import random

class ApiHome(View):
    def get(self, request):
        return render(request, 'appApi/index.html')
    def post(self, request):
        length_gen = request.POST["gen_length"]
        print(length_gen)
        amount_gen = request.POST["gen_amount"]
        print(amount_gen)
        data_chars = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
        data_pwds = []
        for psw in range(int(amount_gen)):
            data_pwds.append("".join(random.sample(data_chars, int(length_gen))))
        print(data_pwds)
        
            
        return JsonResponse({
                            'status' : 'ok',
                            'data' : data_pwds
                            })