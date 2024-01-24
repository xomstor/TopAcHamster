from django.contrib import admin
from .models import ContentBanner, AboutMe, Documents
from django.core.exceptions import ValidationError

@admin.register(ContentBanner)
class ContentBannerAdmin(admin.ModelAdmin):

    list_display = ['title', 'desc', 'number',]
    list_display_links = ['title', 'desc']
    list_editable = ['number',]

    def clean(self):
        super().clean()
        if ContentBanner.objects.count() > 3 and not self.pk:
            raise ValidationError("Максимальное кол-во записей достигнуто. Всего доступно: 3")
        
    def __str__(self):
        return self.title
    
    class Meta:
        model = ContentBanner
        verbose_name = 'Контент'
        verbose_name_plural = 'Баннер'
        
@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):

    list_display = ['fio', 'desc', 'expert', 'photo',]
    list_display_links = ['fio', 'desc','photo',]
    list_editable = [ 'expert',]

    def clean(self):
        super().clean()
        if AboutMe.objects.count() > 1 and not self.pk:
            raise ValidationError("Максимальное кол-во записей достигнуто. Всего доступно: 1")
        
    def __str__(self):
        return self.fio
    
    class Meta:
        model = AboutMe
        verbose_name = 'Обо мне'
        verbose_name_plural = 'Обо мне'
     
@admin.register(Documents)        
class DocumentsAdmin(admin.ModelAdmin):
    list_display = ['title', 'file',]
    list_display_links = ['title', 'file',]
    
    class Meta:
        model = Documents
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'