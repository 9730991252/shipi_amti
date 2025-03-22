from django.shortcuts import render, redirect

from django.db.models import Avg, Sum, Min, Max
from sunil.models import *
from owner.models import *
from order.models import *
from customer.models import *
from django.contrib import messages
from datetime import date
# Create your models here.

def view_customer_order(request, order_filter):
    if request.session.has_key('customer_mobile'):
        mobile = request.session['customer_mobile']
        customer = Customer.objects.filter(mobile=mobile,status=1).first()
        if 'add_reviev'in request.POST:
            i_id = request.POST.get('id')
            ratings = request.POST.get('ratings')
            title = request.POST.get('title')
            contant = request.POST.get('contant')
            r = rattings.objects.filter(item_id=i_id,customer_id=customer.id).first()
            if r:
                r.item_id = i_id
                r.customer_id = customer.id
                r.reviev_title = title
                r.reviev_description = contant
                r.star = ratings
                r.save()
            else:
                rattings(
                    item_id = i_id,
                    customer_id = customer.id,
                    reviev_title = title,
                    reviev_description = contant,
                    star = ratings,
                ).save()
            messages.success(request,"आपली रेव्ह्यू सबमिट केली गेली आहे")
            return redirect(f'/view_customer_order/{order_filter}')

    else:
        return redirect('/')
    contaxt={
        'customer':customer,
        'order_detail':Order_detail.objects.filter(order_filter=order_filter),
        'order_master':OrderMaster.objects.filter(order_filter=order_filter).first(),
    }
    return render(request, 'home/view_customer_order.html', contaxt)
    
def get_session_id(request):
    return request.session.session_key

def index(request):
    customer = ''
    customer_id = 0
    total_amount = 0
        
    session_id = get_session_id(request)
    
    total_amount = total_price(session_id)
                
    c = Cart.objects.all()
    for c in c:
        if c.date != date.today():
            c.delete()
        else:
            print('no')
    it = []
    for i in Item.objects.filter(status=1):
        r = rattings.objects.filter(item_id=i.id)
        avrage_r = r.aggregate(Avg('star'))
                
        total_r = r.count() 
        
        avg = avrage_r['star__avg'] if avrage_r['star__avg'] else 0
        
        it.append({
            'id':i.id,
            'name':i.name,
            'description':i.description,
            'youtube_url':i.youtube_url,
            'image1':i.image1,
            'image2':i.image2,
            'image3':i.image3,
            'image4':i.image4,
            'image5':i.image5,
            'status':i.status,
            
            
            'average_ratings': avg if avg is not 0 else '',
            'total_r':total_r if total_r is not 0 else '',
            
            'all_r':rattings.objects.filter(item_id=i.id),
            
            '1_star_per':round(float(r.filter(item_id=i.id, star=1).count())*(100/total_r)) if total_r != 0 else 0,
            '2_star_per':round(float(r.filter(item_id=i.id, star=2).count())*(100/total_r)) if total_r != 0 else 0,
            '3_star_per':round(float(r.filter(item_id=i.id, star=3).count())*(100/total_r)) if total_r != 0 else 0,
            '4_star_per':round(float(r.filter(item_id=i.id, star=4).count())*(100/total_r)) if total_r != 0 else 0,
            '5_star_per':round(float(r.filter(item_id=i.id, star=5).count())*(100/total_r)) if total_r != 0 else 0,
            
        })
                        
    contaxt={
        'category': Category.objects.filter(status=1),
        'item':it,
        'customer':customer,
        'total_amount':total_amount,
        'cart_qty':Cart.objects.filter(session_id=session_id).count(),
        'i':Item.objects.all().first()
    }
    return render(request, 'home/index.html', contaxt)

def order(request):
    customer = ''
    orderMaster = ''
    if request.session.has_key('customer_mobile'):
        mobile = request.session['customer_mobile']
        customer = Customer.objects.filter(mobile=mobile,status=1).first()
        orderMaster = OrderMaster.objects.filter(customer_id=customer.id).order_by('-id')
    if 'check_mobile'in request.POST:
        mobile = request.POST.get('mobile')
        if mobile:
            c = Customer.objects.filter(mobile=mobile,status=1).first()
            if c:
                request.session['customer_mobile'] = c.mobile
                print('Customer')
            else:
                messages.warning(request,"अद्याप तुमची एकही Order नाही")
        return redirect('/order/')
    contaxt={
        'customer':customer,
        'order_master':orderMaster,
    }
    return render(request, 'home/order.html', contaxt)

def total_price(session_id):
    cart = Cart.objects.filter(session_id=session_id)
    total_amount = 0
    for c in cart:
        total_amount += int(c.qty) * int(c.price_and_weight.price)
    return total_amount

def login(request):
    if request.session.has_key('owner_mobile'):
        return redirect('owner_home')
    if request.method == 'POST':
        mobile = request.POST.get('number')
        pin = request.POST.get('pin')
        e = Employee.objects.filter(mobile=mobile,pin=pin,status=1)
        if e:
            request.session['owner_mobile'] = request.POST["number"]
            return redirect('owner_home')
        else:
            return redirect('/')
    return render(request, 'home/login.html')

def logout(request):
    if request.session.has_key('owner_mobile'):
        del request.session['owner_mobile']
    if request.session.has_key('customer_mobile'):
        del request.session['customer_mobile']
    return redirect('/')