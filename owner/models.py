from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files import File
# Create your models here.
from embed_video.fields import EmbedVideoField 
# Create your models here.
from django.core.files.base import ContentFile
class Category(models.Model):
    name = models.CharField(max_length=255)
    status = models.IntegerField(default=1)
    
class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    youtube_url = EmbedVideoField(null=True)
    image1 = models.ImageField(upload_to='item_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='item_images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='item_images/', blank=True, null=True)
    image4 = models.ImageField(upload_to='item_images/', blank=True, null=True)
    image5 = models.ImageField(upload_to='item_images/', blank=True, null=True)
    status = models.IntegerField(default=1)
    

            
class Price_and_weight(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    price = models.FloatField(default=0)
    weight = models.IntegerField()
    unit = models.CharField(max_length=100)
    sell_minimum_quantity = models.IntegerField(default=1)
    status = models.IntegerField(default=1)
    
# class Category_item(models.Model):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
#     item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
#     status = models.IntegerField(default=1)