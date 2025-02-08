from django.http import JsonResponse
from customer.models import *
from owner.models import *
from order.models import *
from django.template.loader import render_to_string
from home.views import *
def check_customer(request):
    price_and_weight = ''
    customer = ''
    if request.method == 'GET':
        mobile = request.GET['mobile']
        prise_and_weight_id = request.GET['prise_and_weight_id']
        if request.session.has_key('customer_mobile'):
            customer = Customer.objects.filter(mobile=mobile, status=1).first()
        else:
            customer = Customer.objects.filter(mobile=mobile, status=1).first()
            if customer:
                request.session['customer_mobile'] = customer.mobile
            else:
                Customer(
                    mobile=mobile,
                ).save()
                request.session['customer_mobile'] = mobile
            customer = Customer.objects.filter(mobile=mobile, status=1).first()
        price_and_weight = Price_and_weight.objects.filter(id=prise_and_weight_id).first()
        context ={
            'prisce_and_weight_id': prise_and_weight_id,
            'prisce_and_weight':price_and_weight,
            'i':Item.objects.filter(id=price_and_weight.item_id).first(),
            'customer':customer,
            
        }
        t = render_to_string('ajax/check_customer.html', context)
        return JsonResponse({"t": t})
            
def add_to_cart(request):
    if request.method == 'GET':
        item_id = request.GET['item_id']
        qty = request.GET['qty']
        prise_and_weight_id = request.GET['prise_and_weight_id']
        customer_id = request.GET['customer_id']
        customer = ''
        if customer_id:
            customer = Customer.objects.filter(id=customer_id).first()
        # print('item_id =', item_id,   'qty =', qty,   'prise_and_weight_id =', prise_and_weight_id,   'customer_id =', customer_id,  )
        c = Cart.objects.filter(item_id=item_id,price_and_weight_id=prise_and_weight_id, customer_id=customer_id).first()
        if c != None:
            c.qty = qty
            c.save()
        else:
            Cart(
                item_id=item_id,
                qty=qty,
                price_and_weight_id=prise_and_weight_id,
                customer_id=customer_id,
            ).save()
        return JsonResponse({"total_amount": total_price(customer_id), 'cart_qty':Cart.objects.filter(customer_id=customer.id).count()})
    
def cart_qty(request):
    if request.method == 'GET':
        customer_id = request.GET['cid']
        item_id = request.GET['pid']
        qty = request.GET['qty']
        cart = Cart.objects.filter(customer_id=customer_id,item_id=item_id).first()
        if cart:
            cart.qty = qty
            cart.save()
        return JsonResponse({'123':'abc'})
def state(request):
    if request.method == 'GET':
        customer_id = request.GET['id']
        s = request.GET['s']
        c = Customer.objects.filter(id=customer_id).first()
        c.state = s
        c.save()

        return JsonResponse({'123':'abc'})