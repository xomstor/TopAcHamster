from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title',]
    list_display_links = ['title',]

    class Meta:
        model = Category
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'desc', 'price', 'category', 'date']
    list_display_links = ['title',]

    class Meta:
        model = Product
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'