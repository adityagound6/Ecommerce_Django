from django.shortcuts import render, redirect
from store.models import Customer
from django.contrib.auth.hashers import make_password
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        PostData = request.POST
        first_name = PostData.get('first_name')
        last_name = PostData.get('last_name')
        email = PostData.get('email')
        password = PostData.get('password')
        value = dict(first_name=first_name, last_name=last_name, email=email)
        error_message = None

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            email=email,
                            password=password)

        error_message = self.validation_customer(customer)

        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect("index")
        else:
            data = {'error': error_message, 'value': value}
            return render(request, 'signup.html', data)

    def validation_customer(self, customer):
        error_message = None
        if not customer.first_name:
            error_message = "First Name is required"
        elif len(customer.first_name) < 4:
            error_message = 'must be character'
        elif not customer.last_name:
            error_message = "Last name required"
        elif len(customer.last_name) < 4:
            error_message = "last name must be 4 character"
        elif not customer.email:
            error_message = "email required"
        elif not customer.password:
            error_message = "password required"
        elif len(customer.password) < 8:
            error_message = "last name must be 4 character"
        elif customer.isExists():
            error_message = "Already exit"
        return error_message
