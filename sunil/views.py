from django.shortcuts import redirect, render
from . models import *
# Create your views here.
def sunil_login(request):
    if request.method == 'POST':
        a =int(request.POST["number"])
        b =int(request.POST["pin"])
        s = a+b
        if s == 11000 :
            request.session['sunil_mobile'] = s
            return redirect('sunil_home')
        else:
            return redirect('sunil_login')
    return render(request, 'sunil/sunil_login.html')


def sunil_home(request):
    if request.session.has_key('sunil_mobile'):
        if 'Add_Employee'in request.POST:
            name = request.POST.get('name')
            mobile = request.POST.get('mobile')
            pin = request.POST.get('pin')
            Employee(name=name, mobile=mobile, pin=pin).save()
            return redirect('sunil_home')
        if 'Edit_Employee'in request.POST:
            name = request.POST.get('name')
            mobile = request.POST.get('mobile')
            pin = request.POST.get('pin')
            id = request.POST.get('id')
            e = Employee.objects.filter(id=id).first()
            e.name = name
            e.mobile = mobile
            e.pin = pin
            e.save()
            return redirect('sunil_home')
        if 'active'in request.POST:
            id = request.POST.get('id')
            e = Employee.objects.filter(id=id).first()
            e.status = 0
            e.save()
            return redirect('sunil_home')
        if 'deactive'in request.POST:
            id = request.POST.get('id')
            e = Employee.objects.filter(id=id).first()
            e.status = 1
            e.save()
            return redirect('sunil_home')
        context={
            'employee':Employee.objects.all(),
        }
        return render(request, 'sunil/sunil_home.html', context)
    else:
        return redirect('sunil_login')