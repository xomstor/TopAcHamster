from django.db import models
from django.core.exceptions import ValidationError
import datetime


class ContentBanner(models.Model):
    title = models.CharField(
        verbose_name="Название",
        max_length=100,
        null=False
    )
    desc = models.TextField(
        verbose_name="Описание",
        null=False
    )
    number = models.IntegerField(
        verbose_name="Порядковый номер",
        null=True,
        blank=True
    )
    def clean(self):
        super().clean()
        if ContentBanner.objects.count() > 3 and not self.pk:
            raise ValidationError("Максимальное кол-во записей достигнуто. Всего доступно: 3")
        
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Контент'
        verbose_name_plural = 'Баннер'
        
class AboutMe(models.Model):
    fio = models.CharField(
        verbose_name="Фамилия Имя Отчество",
        max_length=200,
        null=False
    )
    desc = models.TextField(
        verbose_name="Описание (Расскажите о себе обо мне)",
        null=False
    )
    expert = models.CharField(
        verbose_name="Должность (позиция)",
        max_length=200,
        null=False
    )
    photo = models.ImageField(
        verbose_name="Фото",
        null=False,
        upload_to = "photos/%Y/%m/%d/"
    )
    def __str__(self):
        return self.fio
    
    def clean(self):
        super().clean()
        if AboutMe.objects.count() > 1 and not self.pk:
            raise ValidationError("Максимальное кол-во записей достигнуто. Всего доступно: 1")
        
    class Meta:
        verbose_name = 'Информация'
        verbose_name_plural = 'Обо мне'
        
class Documents(models.Model):
    title = models.CharField(
        verbose_name="Название (название документа)",
        max_length=100,
        null=False
    )
    file = models.FileField(
        verbose_name="Файл (документ)",
        null=True,
        blank = True,
        upload_to = "documents/%Y/%m/%d/"
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'