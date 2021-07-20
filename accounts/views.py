from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Order, Customer

# Create your views here.

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()

    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders, 
            'customers': customers, 
            'delivered': delivered, 
            'pending': pending, 
            'total_orders': total_orders,
            'total_customers': total_customers}

    return render(request,'accounts/dashboard.html', context)

def products(request):

    products = Product.objects.all()

    return render(request,'accounts/products.html',{'products':products})

def customers(request, pk_test):

    customers = Customer.objects.get(id=pk_test)
    orders = customers.order_set.all()
    order_count = orders.count()

    context = {'customers': customers, 'orders':orders, 'order_count':order_count}

    return render(request,'accounts/customers.html', context)
 