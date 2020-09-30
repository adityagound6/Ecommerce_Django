from django.shortcuts import render
from .models import Product
from django.http import HttpResponse ,HttpRequest

# Create your views here.
def index(request):
    products = Product.get_all_products()
    # print(products)
    return render(request, 'index.html', {'products': products})
