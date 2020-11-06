from django.contrib import admin
from .models.product import Product
from .models.category import Category
from  .models.customer import Customer
from .models.order import Order

# Register your models here.


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Product, AdminProduct),
admin.site.register(Category, AdminCategory)
admin.site.register(Customer)
admin.site.register(Order)
