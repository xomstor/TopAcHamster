from django.shortcuts import render
from django.views import View
from .models import ProductShop
from django.http import JsonResponse, HttpResponse

class HomePage(View):
    def get(self, request):
        obj_products = list(ProductShop.objects.values('id', 'title', 'price', 'count'))
        return render(request, 'appShop/home.html', {
            'products': obj_products
            })
    def post(self, request):
        product_id = request.POST['id']
        key_backed = request.session.get('backed')
        if key_backed is None:
            request.session['backed'] = [product_id]
        else:
            request.session['backed'] = list(key_backed) + [product_id]
        print(request.session.get('backed'))
        return JsonResponse({})

class MethodDjangoPost(View):
    def post(self, request):
        janr = request.POST['janr']
        title = request.POST['title']
        price = request.POST['price']
        return JsonResponse({})
    
class MethodAjaxPost(View):
    def post(self, request):
        text = request.POST['text']
        return JsonResponse({})
    