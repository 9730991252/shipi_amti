from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('order/', views.order, name='order'),
    path('view_customer_order/<int:order_filter>', views.view_customer_order, name='view_customer_order')
]