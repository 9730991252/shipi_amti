from django.db import models
from customer.models import *
from owner.models import *
from sunil.models import *
# Create your models here.
class Cart(models.Model):
    session_id = models.CharField(max_length=100, null=True, blank=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    price_and_weight = models.ForeignKey(Price_and_weight, on_delete=models.CASCADE, null=True)
    qty = models.IntegerField()
    date = models.DateField(auto_now_add=True, null=True)
    
    
    
STATUS_CHOICES = (
  ('Accepted','Accepted'),
  ('Packed','Packed'),
  ('On The Way','On The Way'),
  ('Delivered','Delivered'),
  ('Cancel','Cancel'),
  ('Pending','Pending'),

)
class OrderMaster(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT,default=True)
    status = models.CharField(choices=STATUS_CHOICES,default='Pending',max_length=50)
    total_amount=models.FloatField(default=0,null=True)
    order_filter=models.IntegerField(default=True)
    date=models.DateField(auto_now_add=True,null=True)
    ordered_date = models.DateTimeField(auto_now_add=True,null=True)
    accepted_by = models.ForeignKey(Employee,on_delete=models.PROTECT, blank=True, null=True)

class Order_detail(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT,default=True)
    item = models.ForeignKey(Item,on_delete=models.PROTECT,default=True)
    price=models.FloatField(default=0)
    weight = models.IntegerField(default=0)
    unit = models.CharField(max_length=100, null=True, blank=True)
    qty = models.IntegerField(default=1) 
    order_filter=models.IntegerField(default=True)
    date=models.DateField(auto_now_add=True,null=True)
    ordered_date = models.DateTimeField(auto_now_add=True,null=True)