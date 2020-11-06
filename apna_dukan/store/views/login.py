from django.shortcuts import render, redirect
from store.models import Customer
from django.contrib.auth.hashers import check_password
from django.views import View


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                request.session['email'] = customer.email
                return redirect('index')
            else:
                error_message = "Invalid"

        else:
            error_message = "Invalid"
        return render(request, 'login.html', {'error': error_message})


def logout(request):
    request.session.clear()
    return redirect('index')