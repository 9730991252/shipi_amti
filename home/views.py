from django.shortcuts import render, redirect

from django.db.models import Avg, Sum, Min, Max
from sunil.models import *
from owner.models import *
from order.models import *
from customer.models import *
from django.contrib import messages 
# Create your models here.

def view_customer_order(request, order_filter):
    if request.session.has_key('customer_mobile'):
        mobile = request.session['customer_mobile']
        customer = Customer.objects.filter(mobile=mobile,status=1).first()
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
            
                        
    contaxt={
        'category': Category.objects.filter(status=1),
        'item':Item.objects.filter(status=1),
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
    if 'mobile'in request.POST:
        mobile = request.POST.get('mobile')
        if mobile:
            c = Customer.objects.filter(mobile=mobile,status=1).first()
            if c:
                request.session['customer_mobile'] = c.mobile
            else:
                messages.warning(request,"अद्याप तुमची एकही Order नाही")
        return redirect('order')
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