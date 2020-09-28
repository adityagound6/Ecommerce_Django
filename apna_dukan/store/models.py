from django.db import models
#from .models import Category



class Category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
# Create your models here.



class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    description=models.CharField(max_length=100,default='')
    image=models.ImageField(upload_to='products/')
    category=models.ForeignKey(Category , on_delete=models.CASCADE, default=1)
