from django import template
from django.db.models import Avg, Sum, Min, Max
from math import *
import math
from datetime import date
from owner.models import *

register = template.Library()

@register.inclusion_tag('inclusion_tag/home/price_and_weight.html')
def price_and_weight(item_id):
    p = Price_and_weight.objects.filter(item_id=item_id, status=1).first()
    if p:
        return{
            'weight':p.weight,
            'price':p.price,
            'unit':p.unit,
            'item_id':item_id,
            'price_and_weight':Price_and_weight.objects.filter(item_id=item_id, status=1)
        }