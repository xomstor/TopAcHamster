from django.db import models
import datetime
from tinymce.models import HTMLField



class PubNews(models.Model):
    content = HTMLField('Содержание', null=False)
    date_time = models.DateTimeField('дата и время публикации', auto_now_add=True, null = False)
# default = datetime.datetime.now
    url_name = models.CharField('url, имя ссылки', max_length=25, null=False, unique=True)
    def __str__(self):
        return self.url_name
    
    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"
        
