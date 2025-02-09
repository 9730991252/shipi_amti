from django.shortcuts import render, redirect
from .models import *
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
import io
import time
# Create your views here.
def hotel_home(request):
    if request.session.has_key('owner_mobile'):
        context={
        }
        return render(request, 'hotel/hotel_home.html')
    else:
        return redirect('login')
    
def hotel_item(request):
    if request.session.has_key('owner_mobile'):
        if request.method == 'POST':
            name = request.POST.get('name')
            hotel_Item(
                name=name,
                ).save()
            return redirect('hotel_item')
        context = {
            'items': hotel_Item.objects.all(),        }
        return render(request, 'hotel/hotel_item.html', context)
    else:
        return redirect('login')
    