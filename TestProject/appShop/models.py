from django.db import models

class ProductShop(models.Model):
    title = models.CharField('Имя товара', max_length=100)
    price = models.FloatField('Цена', null=False, default=0)
    # category = models.CharField('Категория', max_length=100)
    description = models.TextField('Описание', null=True)
    # image = models.ImageField('Изображение', upload_to='images/')
    count=models.IntegerField('Количество товара на складе', null=False, default=0)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'