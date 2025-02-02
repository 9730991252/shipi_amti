from django.db import models

# Create your models here.
class Customer (models.Model):
    mobile=models.IntegerField(null=True,blank=True)
    name=models.CharField(max_length=100,null=True,blank=True)
    pin_code = models.IntegerField(null=True,blank=True)    
    house_no=models.CharField(max_length=100,null=True,blank=True)
    post=models.CharField(max_length=100,null=True,blank=True)
    landmark=models.CharField(max_length=100,null=True,blank=True)
    taluka=models.CharField(max_length=100,null=True,blank=True)
    district=models.CharField(max_length=100,null=True,blank=True)
    state_name=models.CharField(max_length=100,null=True,blank=True)
    state=models.CharField(max_length=100,default=1)
    date=models.DateField(auto_now_add=True,null=True)
    status = models.IntegerField(default=1)