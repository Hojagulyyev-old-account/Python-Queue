from django.db import models
from datetime import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError
# Create your models here.
# def validate_even(value):
#     if value != '2021-06-25':
#         raise ValidationError(
#             '%(value)s is not an even number',
#             params={'value': value},
#         )

# , validators=[validate_even]

class Cell(models.Model):
    date = models.DateField(default=timezone.now)
    time = models.CharField(max_length=6)

    def __str__(self):
        return f'{self.time} {self.date}'

    def datepublished(self):
        return self.date.strftime('%d.%m.%Y')

    class Meta:
        ordering = ('date',)


class Example(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField()
    image = models.ImageField(upload_to='media/example/images', blank=True)
    price = models.PositiveSmallIntegerField(default=0)
    in_stock = models.BooleanField(default=False)

    def imageURL(self):
        if not self.image:
            return "No image"
        else:
            return self.image.url

    def __str__(self):
        return self.title
