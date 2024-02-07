from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
from django.db.models import Q
from .models import Product, PhotoProduct, Category, SubCategory

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
    
class CategoriesPage(View):
    def get(self, request):
        data_sub = SubCategory.objects.all()
        data = {
            
        }
        for sub in data_sub:
            if sub.category.title not in data:
                data.update({
                    sub.category.title: {
                        sub.id : sub.title
                    }
                    })
            else:
                # data[sub.category.title][sub.id] = sub.title
                data[sub.category.title].update({
                    sub.id : sub.title
                })
        print(data)
        return render(request, 'appKey/home/categories.html', {'object':data})
    
class ProductPage(View):
    def get(self, request, id):
        sub_category = SubCategory.objects.filter(id=id)
        if sub_category:
            data = {
                'title' : sub_category.first().title,
                'cards' : Product.objects.filter(subcategory=id).values('id', 'title', 'price', 'currency')    #.values_list('title', flat=True)
            }
            print(data)
            return render(request, 'appKey/home/product.html', data)
        else:
            return redirect('url-categories')

        