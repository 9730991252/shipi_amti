from django.db import models

# Create your models here.
class hotel_Item(models.Model):
    name = models.CharField(max_length=100)
    status = models.IntegerField(default=1)