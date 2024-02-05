from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
from django.db.models import Q
from .models import Product, PhotoProduct, Category

class HomeKey(View):
    def get(self, request):
        data = {
            'products': Product.objects.all(),
            'photos': PhotoProduct.objects.filter(photoforproduct__isnull=True)
        }
        return render(request, 'appKey/product/index.html', data)
    def post(self, request):
        if request.POST["method"] == "addCategory":
           Category.objects.create(
               title = request.POST["text"]
           )
        #    Category.objects.filter( # - СНАЧАЛА НАДО НАЙТИ ЧТО ОБНОВИТЬ И УДАЛИТЬ
        #        title = request.POST["text"]
        #    )
        #    Category.objects.update(
        #        title = request.POST["text"]
        #    )
        #    Category.objects.delete(
        #        title = request.POST["text"]               
        #    )
        return redirect('url-home')
    