from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Product
from .models import Category
from .models import Customer


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
    if request.method=='GET':
        return render(request, 'signup.html')
    else:
        PostData=request.POST
        first_name=PostData.get('first_name')
        last_name = PostData.get('last_name')
        email = PostData.get('email')
        password = PostData.get('password')
        customer=Customer(first_name=first_name,
                          last_name=last_name,
                          email=email,
                          password=password)
        customer.register()
        return HttpResponse("signup")

