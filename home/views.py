from django.shortcuts import render, redirect
from django.db.models import Avg, Sum, Min, Max
from django.contrib import messages
from datetime import date
# Create your models here.
def index(request):
   
    return render(request, 'home/index.html', )
