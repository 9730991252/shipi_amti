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

from django.core.files.base import ContentFile

def convert_image_to_webp(image_field):
    try:
        # Open the image using Pillow
        image = Image.open(image_field)
        # Create a BytesIO object to hold the WebP data
        webp_io = BytesIO()
        # Save the image in WebP format to the BytesIO object
        image.save(webp_io, format='WEBP', quality=50)
        # Create a ContentFile from the BytesIO object
        webp_content = ContentFile(webp_io.getvalue(), name=f"{image_field.name.rsplit('.', 1)[0]}.webp")
        return webp_content
    except Exception as e:
        print(f"Error converting image to WebP: {e}")
        return None
    
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
        if self.image1:
            webp_image = convert_image_to_webp(self.image1)
            self.image1.save(webp_image.name, webp_image, save=False)

        if self.image2:
            webp_image = convert_image_to_webp(self.image2)
            self.image2.save(webp_image.name, webp_image, save=False)
            
        if self.image3:
            webp_image = convert_image_to_webp(self.image3)
            self.image3.save(webp_image.name, webp_image, save=False)
        
        if self.image4:
            webp_image = convert_image_to_webp(self.image4)
            self.image4.save(webp_image.name, webp_image, save=False)
            
        if self.image5:
            webp_image = convert_image_to_webp(self.image5)
            self.image5.save(webp_image.name, webp_image, save=False)
        
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