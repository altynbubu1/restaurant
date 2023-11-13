from django.shortcuts import render
from main.models import Employee, Menu, Restaurant, Restauran, Restaura, New_dishes


def testing(request):
    employes = Employee.objects.all()
    menu = Menu.objects.all()
    restaurant = Restaurant.objects.all()
    restauran = Restauran.objects.all()
    restaura = Restaura.objects.all()
    new_dishes = New_dishes.objects.all()
    context = {
        'employes': employes,
        'menu': menu,
        'restaurant': restaurant,
        'restauran': restauran,
        'restaura': restaura,
        'new_dishes': new_dishes,

    }
    return render(request, 'main/index.html', context)


def employees(request):
    employes = Employee.objects.all()
    context = {
        'employes': employes,
    }
    return render(request, 'main/employees.html', context)


def menu(request):
    menu = Menu.objects.all()
    context = {
        'menu': menu,
    }
    return render(request, 'main/menu.html', context)


def zakaz(request):
    return render(request, 'main/zakaz.html')


def about(request):
    return render(request, 'main/about.html')
