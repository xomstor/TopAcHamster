from django.db import models

class Category(models.Model):
    title = models.TextField(
    "Категория",
    null=False,
    help_text="Например: квартира"   
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        
class Product(models.Model):
    title = models.TextField(
        "Название",
        null=False,
        help_text="Например: Продаю земельный участок"
    )
    desc = models.TextField(
        "Описание",
        null=True,
        blank=True
    )
    price = models.FloatField(
        "Стоимость",
        null=False
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT
        )
    date = models.DateTimeField(
        auto_now_add=True
        )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'