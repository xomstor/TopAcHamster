from django.db import models

class ContentNews(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок новости", null=False)
    name_url = models.CharField(max_length=255, verbose_name="Ссылка на новость", null=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
        # return super().__str__()
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"