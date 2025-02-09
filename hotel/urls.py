from django.urls import path
from . import views

urlpatterns = [
    path('hotel_home/', views.hotel_home, name='hotel_home'),
    path('hotel_item/', views.hotel_item, name='hotel_item'),
]