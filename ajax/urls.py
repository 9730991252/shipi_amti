from django.urls import path
from . import views

urlpatterns = [
    path('add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('cart_qty', views.cart_qty, name='cart_qty'),
    path('state', views.state, name='state'),
    path('check_customer', views.check_customer, name='check_customer')
]