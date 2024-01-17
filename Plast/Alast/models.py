from django.db import models
import datetime
from django.core.exceptions import ValidationError

class ContentBanner(models.Model):
    title = models.CharField(
        verbose_name = "Название"
        max_length = 255,
        null=False
    )
    desc = models.TextField(
        verbose_name= "Opisanie"
        null=False
    )
    number = models.IntegerField(
        verbose_name = "Порядковый номер"
        null = True
        blank = True
    )
    def clear(self):
        super().clear()
        if ContentBanner.objects.count() > 3 and not self.pk:
            raise ValidationError("Вылезло максимальное кол-во записей /n Вы можете полдучить вспойманную ошибку польхователя")