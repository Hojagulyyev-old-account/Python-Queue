from django.db import models
from datetime import datetime
# Create your models here.
class Cell(models.Model):
    date = models.DateField(default=datetime.now())
    time = models.CharField(max_length=6)

    def __str__(self):
        return f'{self.time} {self.date}'

    def datepublished(self):
        return self.date.strftime('%d.%m.%Y')

    class Meta:
        ordering = ('date',)
