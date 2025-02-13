from django.shortcuts import render
from home.views import *
from django.views.decorators.csrf import csrf_exempt
from django import template
from home.templatetags.home_tag import *
register = template.Library()
# Create your views here.
def pending_order(request):
    if request.session.has_key('owner_mobile'):
        mobile = request.session['owner_mobile']
        e = Employee.objects.filter(mobile=mobile).first()
        context={
            'employee':e,
            'orders':OrderMaster.objects.filter(status='Pending').order_by('-id')
        }
        return render(request, 'order/pending_order.html',context)
    else:
        return redirect('login')
    
def delivered(request):
    if request.session.has_key('owner_mobile'):
        mobile = request.session['owner_mobile']
        e = Employee.objects.filter(mobile=mobile).first()
        context={
            'employee':e,
            'orders':OrderMaster.objects.filter(status='Delivered').order_by('-id')
        }
        return render(request, 'order/delivered.html',context)
    else:
        return redirect('login')
    
def accepted(request):
    if request.session.has_key('owner_mobile'):
        mobile = request.session['owner_mobile']
        e = Employee.objects.filter(mobile=mobile).first()
        order = OrderMaster.objects.filter(status='Accepted').order_by('-id')

        
        context={
            'employee':e,
            'orders':order
        }
        return render(request, 'order/accepted.html',context)
    else:
        return redirect('login')
    
    
@csrf_exempt
def download_invoice(request, order_filter):
    if request.session.has_key('owner_mobile'):
        mobile = request.session['owner_mobile']
        e = Employee.objects.filter(mobile=mobile).first()

        
        context={
            'employee':e,
            'order_master':OrderMaster.objects.filter(order_filter=order_filter).first(),
            'order_details':Order_detail.objects.filter(order_filter=order_filter),
        } 
        return render(request, 'order/download_invoice.html',context)
    else:
        return redirect('login')
    
@csrf_exempt
def delivered_view_order(request, order_filter):
    if request.session.has_key('owner_mobile'):
        mobile = request.session['owner_mobile']
        e = Employee.objects.filter(mobile=mobile).first()
        if 'Cancel'in request.POST:
            a = OrderMaster.objects.filter(order_filter=order_filter).first()
            a.accepted_by_id = e.id
            a.status = 'Cancel'
            a.save()
            return redirect('cancel_view_order', order_filter=order_filter)
        order = OrderMaster.objects.filter(order_filter=order_filter).first()
        context={
            'employee':e,
            'order_master':order,
            'order_details':Order_detail.objects.filter(order_filter=order_filter)
        }
        return render(request, 'order/delivered_view_order.html',context)
    else:
        return redirect('login')
@csrf_exempt
def accepted_view_order(request, order_filter):
    if request.session.has_key('owner_mobile'):
        mobile = request.session['owner_mobile']
        e = Employee.objects.filter(mobile=mobile).first()
        if 'Delivered'in request.POST:
            a = OrderMaster.objects.filter(order_filter=order_filter).first()
            a.accepted_by_id = e.id
            a.status = 'Delivered'
            a.save()
            return redirect('delivered_view_order', order_filter=order_filter)
        if 'Cancel'in request.POST:
            a = OrderMaster.objects.filter(order_filter=order_filter).first()
            a.accepted_by_id = e.id
            a.status = 'Cancel'
            a.save()
            return redirect('cancel_view_order', order_filter=order_filter)
        order = OrderMaster.objects.filter(order_filter=order_filter).first()
        if order.status == 'Delivered':
            return redirect('delivered_view_order', order_filter=order_filter)
        context={
            'employee':e,
            'order_master':order,
            'order_details':Order_detail.objects.filter(order_filter=order_filter)
        }
        return render(request, 'order/accepted_view_order.html',context)
    else:
        return redirect('login')
    
@csrf_exempt
def pending_view_order(request, order_filter):
    if request.session.has_key('owner_mobile'):
        mobile = request.session['owner_mobile']
        e = Employee.objects.filter(mobile=mobile).first()
        if 'accept'in request.POST:
            a = OrderMaster.objects.filter(order_filter=order_filter).first()
            a.accepted_by_id = e.id
            a.status = 'Accepted'
            a.save()
            return redirect('accepted_view_order', order_filter=order_filter)
        if 'cancel'in request.POST:
            a = OrderMaster.objects.filter(order_filter=order_filter).first()
            a.accepted_by_id = e.id
            a.status = 'Cancel'
            a.save()
            return redirect('pending_view_order', order_filter=order_filter)
        
        context={
            'employee':e,
            'order_master':OrderMaster.objects.filter(order_filter=order_filter).first(),
            'order_details':Order_detail.objects.filter(order_filter=order_filter)
        }
        return render(request, 'order/pending_view_order.html',context)
    else:
        return redirect('login')
    
def order(request):
    if request.session.has_key('owner_mobile'):
        context={
        }
        return render(request, 'order/order.html')
    else:
        return redirect('login')

@csrf_exempt
def cart(request):
    session_id = get_session_id(request)
    cart = ''
    total_amount = 0
    total_amount_sub = 0
    total_amount = total_price(session_id)
    cart = Cart.objects.filter(session_id=session_id)
    if cart:
        pass
    else:
        return redirect('/')
    if 'Remove'in request.POST:
        cart_id = request.POST.get('cart_id')
        Cart.objects.filter(id=cart_id).delete()
        return redirect('cart')
    if 'Add_address'in request.POST:
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        
        request.session.flush()
        request.session['customer_mobile'] = mobile
        
        pin_code = request.POST.get('pin_code')
        house_no = request.POST.get('house_no')
        post = request.POST.get('post')
        landmark = request.POST.get('landmark')
        taluka = request.POST.get('taluka')
        district = request.POST.get('district')
        state_name = request.POST.get('state_name')
        customer = Customer.objects.filter(mobile=mobile).first()
        customer.name = name
        customer.pin_code = pin_code
        customer.house_no = house_no
        customer.post = post
        customer.landmark = landmark
        customer.taluka = taluka
        customer.district = district
        customer.state_name = state_name
        customer.save()
        order_filter = int(OrderMaster.objects.all().count()) +1
        
        OrderMaster(
            customer_id=customer.id,
            total_amount=total_amount,
            order_filter=order_filter,
        ).save()
        for c in cart:
            Order_detail(
                customer_id=customer.id,
                item_id=c.item.id,
                price=c.price_and_weight.price,
                weight=c.price_and_weight.weight,
                unit=c.price_and_weight.unit,
                qty=c.qty,
                order_filter=order_filter,
            ).save()
        Cart.objects.filter(session_id=session_id).delete()
        return redirect('/')
        
    contaxt={
        'cart':cart,
        'total_amount_sub':total_amount
    }
    return render(request, 'order/cart.html', contaxt)