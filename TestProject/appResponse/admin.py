from django.contrib import admin
from .models import GenerateNumber, GenerateDate
import random, datetime

@admin.register(GenerateNumber)
class GenerateNumberAdmin(admin.ModelAdmin):
    list_display = ('id','number', 'status')
    list_display_links = ('number', )
    list_filter = ('status',)
    list_editable = ('status',)
    list_per_page = 10
    search_fields = ('number',)
    
    class Meta:
        model = GenerateNumber
        verbose_name = 'Число'
        verbose_name_plural = 'Числа'
    
@admin.register(GenerateDate)
class GenerateDateAdmin(admin.ModelAdmin):
    list_display = ('id','date', 'status',)
    list_display_links = ('id','date',)
    list_filter = ('status',)
    list_editable = ('status',)
    list_per_page = 10
    search_fields = ('date',)
    readonly_fields = ('date',)
    
    class Meta:
        model = GenerateDate
        verbose_name = 'Дату и время'
        verbose_name_plural = 'Даты и времена'
        
