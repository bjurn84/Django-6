from django.shortcuts import render
from .models import Client, Product, Order

def client_detail(request, client_id):
    client = Client.objects.get(pk=client_id)
    return render(request, 'client_detail.html', {'client': client})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def order_detail(request, order_id):
    order = Order.objects.get(pk=order_id)
    return render(request, 'order_detail.html', {'order': order})