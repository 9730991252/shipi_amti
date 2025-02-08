from django.shortcuts import render, redirect
from .models import *
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
import io
import time
# Create your views here.
def owner_home(request):
    if request.session.has_key('owner_mobile'):
        context={
        }
        return render(request, 'owner/owner_home.html')
    else:
        return redirect('login')
    
def item(request):
    if request.session.has_key('owner_mobile'):
        if request.method == 'POST':
            name = request.POST.get('name')
            description = request.POST.get('description')
            img = request.FILES.get('image')
            Item(
                name=name,
                description=description,
                image1 = img,
                ).save()
            return redirect('item')
        context = {
            'items': Item.objects.all(),        }
        return render(request, 'owner/item.html', context)
    else:
        return redirect('login')
    
def category(request):
    if request.session.has_key('owner_mobile'):
        if 'add_category'in request.POST:
            category_name = request.POST.get('name')
            if category_name:
                Category.objects.create(name=category_name)
                return redirect('category')
        if 'edit_category' in request.POST:
            category_id = request.POST.get('id')
            category_name = request.POST.get('name')
            if category_id and category_name:
                category = Category.objects.get(id=category_id)
                category.name = category_name
                category.save()
            return redirect('category')
        if 'active'in request.POST:
            id = request.POST.get('id')
            category = Category.objects.get(id=id)
            category.status = 0
            category.save()
            return redirect('category')
        if 'deactive' in request.POST:
            id = request.POST.get('id')
            category = Category.objects.get(id=id)
            category.status = 1
            category.save()
            return redirect('category')
        
        context = {
            'category': Category.objects.all()
        }
        return render(request, 'owner/category.html', context)
    else:
        return redirect('login')
    

    
@csrf_exempt
def item_detail(request, id):
    if request.session.has_key('owner_mobile'):
        items = Item.objects.filter(id=id).first()
        if 'edit_item_embed_video'in request.POST:
            embed_video = request.POST.get('embed_video')
            items.youtube_url = embed_video
            items.save()
            return redirect('item_detail', id=id)
        if 'edit_item_name'in request.POST:
            new_name = request.POST.get('name')
            if new_name:
                items.name = new_name
                items.save()
                return redirect('item_detail', id=id)
        if 'Add_price_and_weight'in request.POST:
            price = request.POST.get('price')
            weight = request.POST.get('weight')
            unit = request.POST.get('unit')
            sell_minimum_quantity = request.POST.get('sell_minimum_quantity')
            Price_and_weight(
                item_id=id,
                price=price,
                weight=weight,
                unit=unit,
                sell_minimum_quantity=sell_minimum_quantity
                ).save()
            return redirect('item_detail', id=id)
        if 'edit_item_description'in request.POST:
            description = request.POST.get('description')
            items.description = description
            items.save()
            return redirect('item_detail', id=id)
        if 'Edit_price_and_weight'in request.POST:
            p_id = request.POST.get('id')
            price = request.POST.get('price')
            weight = request.POST.get('weight')
            unit = request.POST.get('unit')
            sell_minimum_quantity = request.POST.get('sell_minimum_quantity')
            p = Price_and_weight.objects.get(id=p_id)
            p.price = price
            p.weight = weight
            p.unit = unit
            p.sell_minimum_quantity = sell_minimum_quantity
            p.save()
            return redirect('item_detail', id=id)
        if 'active'in request.POST:
            p_id = request.POST.get('id')
            p = Price_and_weight.objects.get(id=p_id)
            p.status = 0
            p.save()
            return redirect('item_detail', id=id )
        if 'deactive' in request.POST:
            p_id = request.POST.get('id')
            p = Price_and_weight.objects.get(id=p_id)
            p.status = 1
            p.save()
            return redirect('item_detail', id=id )
        if 'Edit_item'in request.POST:            
            image1 = request.FILES.get('image1')
            
            if image1 == None:
                pass
            else:
                items.image1 = image1
                
            image2 = request.FILES.get('image2')
            if image2 is None:
                image2 = items.image2
            else:
                items.image2 = image2
                
            image3 = request.FILES.get('image3')
            if image3 is None:
                image3 = items.image3
            else:
                items.image3 = image3
                
            image4 = request.FILES.get('image4')
            if image4 is None:
                image4 = items.image4
            else:
                items.image4 = image4
                
            image5 = request.FILES.get('image5')
            if image5 is None:
                image5 = items.image5
            else:
                items.image5 = image5
            items.save()
            return redirect('item_detail', id=id)
        if 'select_item_category'in request.POST:
            c_id = request.POST.get('id')
            category_item = Category_item.objects.filter(category_id=c_id,item_id=items.id).first()
            if category_item:
                if category_item.status==0:
                    category_item.status = 1
                    category_item.save()
            else:
                Category_item(
                    category_id=c_id,
                    item_id=items.id,
                ).save()
            return redirect('item_detail', id=id)
        if 'unselect_category'in request.POST:
            c_id = request.POST.get('id')
            category_item = Category_item.objects.filter(category_id=c_id,item_id=items.id).first()
            if category_item:
                if category_item.status==1:
                    category_item.status = 0
                    category_item.save()
            return redirect('item_detail', id=id)
        category=[]
        for c in Category.objects.filter(status=1):
            if Category_item.objects.filter(category_id=c.id,item_id=items.id, status=1).exists():
                category.append({'id': c.id,'name':c.name, 'selected_status': 1})
            else:
                category.append({'id': c.id,'name':c.name, 'selected_status': 0})
        context = {
            'item': items,
            'prise_and_weight':Price_and_weight.objects.filter(item_id=id),
            'category': category

        }
        return render(request, 'owner/item_detail.html', context)
    else:
        return redirect('login')