from django.db import models

class FormUser(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name="Ім'я",
                            null = False,
                            default = "Unknown",
                            help_text="Введіть ваше Ім'я")
    email = models.EmailField(verbose_name="Пошта",
                            null = False,
                            help_text="Введіть вашу пошту")
    age = models.IntegerField(verbose_name="Вік",
                            null = False,
                            help_text="Введіть ваш вік")
    def __str__(self):
        return self.email
    class Meta:
        verbose_name = "Контактну інформацію користувачя"
        verbose_name_plural = "Користувачі - контактні інформації"
    