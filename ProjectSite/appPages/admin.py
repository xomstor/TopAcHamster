from django.contrib import admin
from .models import ContentBanner
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