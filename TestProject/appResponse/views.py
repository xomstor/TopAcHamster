from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views import View
from appResponse.models import GenerateNumber, GenerateDate
from random import random, randint

class ResponsePage(View):
    def get(self, request):
        
        d1 = GenerateNumber.objects.all()
        for d in d1:
            if d.status:
                d.number *= 4
            else:
                d.number /= 2
        generate_numbers = GenerateNumber.objects.all()
        for generate_number in generate_numbers:
            generate_number.save()
        data = {
            
        }
        # data = {
        #     'numbers': [{
        #         'id': generate_number.id,
        #         'number': generate_number.number,
        #         'status': generate_number.status
        #     } for generate_number in generate_numbers]
        # }
        data['generate_numbers'] = list(generate_numbers.values('id', 'number', 'status'))
        print(GenerateNumber.objects.order_by("-number"))
        
        # d_gt = GenerateNumber.objects.filter(number__gt = 100)
        # print("Больше 100",d_gt)
        # d_lt = GenerateNumber.objects.filter(number__lt = 100)
        # print("Меньше 100",d_lt)
        # d_gte = GenerateNumber.objects.filter(number__gte = 100)
        # print("Больше или равно 100",d_gte)
        # d_lte = GenerateNumber.objects.filter(number__lte = 100)
        # print("Меньше или равно 100",d_lte)
        
        print(GenerateNumber.objects.values('number', 'status'))
        print(GenerateNumber.objects.values_list('id', 'status'))
        return JsonResponse(data, safe=False)