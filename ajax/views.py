from django.http import JsonResponse
from customer.models import *
from owner.models import *
from order.models import *
from django.template.loader import render_to_string
from home.views import *
def add_to_cart(request):
    if not request.session.session_key:
        request.session.create()
    if request.method == 'GET':
        item_id = request.GET['item_id']
        # print('item_id:', item_id)
        qty = request.GET['qty']
        prise_and_weight_id = request.GET['prise_and_weight_id']
        session_id = get_session_id(request)
        c = Cart.objects.filter(item_id=item_id,price_and_weight_id=prise_and_weight_id, session_id=session_id).first()
        if c != None:
            c.qty = qty
            c.save()
        else:
            Cart(
                item_id=item_id,
                qty=qty,
                price_and_weight_id=prise_and_weight_id,
                session_id=session_id,
            ).save()
        return JsonResponse({"total_amount": total_price(session_id), 'cart_qty':Cart.objects.filter(session_id=session_id).count()})
    
def check_customer(request):
    if request.method == 'GET':
        mobile = request.GET['mobile']
        c = Customer.objects.filter(mobile=mobile).first()
        if c is None:
            Customer(
                mobile=mobile,
                status=1,
            )
        c = Customer.objects.filter(mobile=mobile).first()
    context={
        'customer':c
    }
    return JsonResponse({'t':render_to_string('ajax/check_customer.html', context)})
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