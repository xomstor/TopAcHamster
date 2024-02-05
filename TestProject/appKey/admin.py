from django.contrib import admin
from .models import Category, Product, SubCategory, PhotoProduct
from django_summernote.admin import SummernoteModelAdmin

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['title',]
#     list_display_links = ['title',]

#     class Meta:
#         model = Category
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Категории'
        
# @admin.register(SubCategory)
# class SubCategoryAdmin(admin.ModelAdmin):
#     list_display = ['id','title', 'category',]
#     list_display_links = ['title',]
#     list_filter = ['category',]

#     class Meta:
#         model = SubCategory
#         verbose_name = 'Подкатегория'
#         verbose_name_plural = 'Подкатегории'
        

        
     
class SubCategoryStaсked(admin.StackedInline):
    model = SubCategory # дочерняя модель
    extra = 1
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubCategoryStaсked,]
    
    class Meta:
        model = Category # название модели - родитель
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class PhotoProductStaсked(admin.StackedInline):
    model = PhotoProduct # дочерняя модель
    extra = 1

@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    summernote_fields = 'desc'
    inlines = [PhotoProductStaсked,]
    list_display = ['id','title', 'price', 'date', 'subcategory', 'currency',]
    list_display_links = ['subcategory', 'title',]
    raw_id_fields = ['subcategory',]
    search_fields = ['title',]
    class Meta:
        model = Product
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
