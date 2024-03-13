from django.db import models
from appPublication.models import PubNews
import datetime

class TableOfUserAgents(models.Model):
    pub_news = models.ForeignKey(PubNews, on_delete=models.CASCADE, null = False, verbose_name="Публикация")
    user_agent = models.TextField(verbose_name="Пользовательский агент", null=True, blank = True)
    user_agent_parse_os = models.TextField(verbose_name="user_agent_parse_os", null=True, blank = True)
    user_agent_parse_browser = models.TextField(verbose_name="user_agent_parse_browser", null=True, blank = True)
    user_agent_parse_is_bot = models.BooleanField(verbose_name="bot?", choices=[(True, 'Yes'), (False, 'No'), (None, 'ХЗ')], default=False, null=True, blank = True)
    user_agent_parse_is_touch = models.BooleanField(verbose_name="тачевое?", choices=[(True, 'Yes'), (False, 'No'), (None, 'ХЗ')], default=False, null=True, blank = True)
    device_type = models.CharField(verbose_name="device_type", max_length=100, choices = [("mobile", "mobile"), ("tablet", "tablet"), ("desktop", "PC")], null=True, blank = True)
    date_time = models.DateTimeField(verbose_name="дата и время публикации", default = datetime.datetime.now, null = False)
    
    def __str__(self):
        return self.pub_news.url_name
    
    class Meta:
        verbose_name = "История (статистика) Пользовательский агент"
        verbose_name_plural = "Просмотры (статистика) Пользовательские агенты"
        
