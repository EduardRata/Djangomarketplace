from django.shortcuts import render
from . models import User, Product, Order
# Create your views here.

def user_list(request):
    users = User.objects.all()
    return render(request, "user_list.html", {"users": users})


def product_list(request):
    products = Product.objects.all()
    return render (request, "product_list.html", {"products": products})


def order_list(request):
    orders = Order.objects.all()
    return render (request, "orders_list.html", {"orders": orders})
