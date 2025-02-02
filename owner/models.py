from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files import File
# Create your models here.
from embed_video.fields import EmbedVideoField 
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    status = models.IntegerField(default=1)
    
def compress(image):
    im = Image.open(image)
    rgb_im = im.convert("RGB")
    
    im_io = BytesIO()
    rgb_im.save(im_io, format=im.format, quality=50)
    new_image = File(im_io, name=image.name)
    return new_image
    
    
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
    
    def save (self, *args, **kwargs):
        new_image1 = compress(self.image1)
        self.image1 = new_image1
        
        if self.image2:
            new_image2 = compress(self.image2)
            self.image2 = new_image2
            
        if self.image3:
            new_image3 = compress(self.image3)
            self.image3 = new_image3
        
        if self.image4:
            new_image4 = compress(self.image4)
            self.image4 = new_image4
        
        if self.image5:
            new_image5 = compress(self.image5)
            self.image5 = new_image5
        
        super().save(*args, **kwargs)

            
class Price_and_weight(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    price = models.FloatField(default=0)
    weight = models.IntegerField()
    unit = models.CharField(max_length=100)
    sell_minimum_quantity = models.IntegerField(default=1)
    status = models.IntegerField(default=1)
    
class Category_item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    status = models.IntegerField(default=1)