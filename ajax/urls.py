from django.urls import path
from . import views

urlpatterns = [
    path('check_customer', views.check_customer, name='check_customer'),
    path('add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('cart_qty', views.cart_qty, name='cart_qty'),
    path('state', views.state, name='state'),
]