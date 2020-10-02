from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Product
from .models import Category


# Create your views here.
def index(request):
    products = None
    categories = Category.get_all_category()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_id(categoryID)
    else:
        products = Product.get_all_products()

    data = {'products': products, 'categories': categories}
    return render(request, 'index.html', data)


def signup(request):
    return render(request, 'signup.html')
