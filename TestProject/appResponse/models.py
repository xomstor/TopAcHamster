from django.db import models
import random, datetime


class GenerateNumber(models.Model):
    number = models.IntegerField("Число", default = 123,)
    status = models.BooleanField("Разрешение",
                                 default = True,
                                 help_text = "Да (активировать) или Нет (деактивировать)",
                                 null = False)
    def save(self, *args, **kwargs):
        if self.pk is None:
            self.number = random.randint(100, 600)
        super().save(*args, **kwargs)
        
    def __int__(self):
        return int(self.number)
    class Meta:
        verbose_name = 'Число'
        verbose_name_plural = 'Числа'
        
class GenerateDate(models.Model):
    date = models.DateTimeField("Дата и время",
                            default = datetime.datetime.now,
                            editable = False,
                            null = False)
    status = models.BooleanField("Разрешение",
                                 default = True,
                                 help_text = "Да (активно) или Нет (неактивно)",
                                 null = True,
                                 blank = True)
    def __str__(self):
        return str(self.date)
    class Meta:
        verbose_name = 'Дату и время'
        verbose_name_plural = 'Даты и времена'