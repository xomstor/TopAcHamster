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
        
class SubCategory(models.Model):
    title = models.CharField(
    "Подкатегория",
    max_length=100,
    null=False
    )
    category = models.ForeignKey(
    Category,
    on_delete=models.PROTECT,
    verbose_name = 'Категория'
    )
    def __str__(self):
        return f'Категории: {self.category.title} | Подкатегория: {self.title}'
    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'        

class Product(models.Model):
    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.PROTECT,
        verbose_name = 'Подкатегория',
        null=False
    )
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
    currency = models.CharField(
        "Валюта",
        max_length=10,
        null=False,
        choices = (
            ('RUB', 'RUB'),
            ('USD', 'USD баксы'),
            ('EUR', 'EUR евреи'),
            ('UAH', 'UAH гривны'),
            ('CNY', 'CNY юань'),
            ('BTC', 'BTC биточки')
        ),
        default="RUB",
    )
    date = models.DateTimeField(
        auto_now_add=True
        )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        