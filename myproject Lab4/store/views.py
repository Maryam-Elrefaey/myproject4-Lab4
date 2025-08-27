from django.shortcuts import render
from .models import Product

# Create your views here.

def home(request):
    return render(request, "home.html")

def store_page(request):
    products = Product.objects.all()
    expensive_products = Product.objects.filter(price__gt=100)
    not_cheap_products = Product.objects.exclude(price__lt=50)  
    products_by_price = Product.objects.order_by('price')
    products_by_price_desc = Product.objects.order_by('-price')
    product_exact = Product.objects.filter(name__exact="Lap")
    product_contains = Product.objects.filter(name__contains="Bag")
    products_in_range = Product.objects.filter(price__range=(10, 200))

    return render(request, "store.html", {
        "products": products,
        "expensive_products": expensive_products,
        "not_cheap_products": not_cheap_products,
        "products_by_price": products_by_price,
        "products_by_price_desc": products_by_price_desc,
        "product_exact": product_exact,
        "product_contains": product_contains,
        "products_in_range": products_in_range,
    })






