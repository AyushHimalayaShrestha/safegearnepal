from django.db import models
from django.utils.text import slugify
import json
# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact_person =models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()
    created_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name =models.CharField(max_length=255)
    slug =models.SlugField(unique=True, max_length=255)
    category =models.CharField(max_length=255)
    price_npr = models.DecimalField(max_digits=10, decimal_places=2)
    landed_cost =models.DecimalField(max_digits=10, decimal_places=2)
    stock =models.PositiveIntegerField(default=0)
    supplier = models.ForeignKey(Supplier,on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='products/')

    #JSON/TEXT field for specifications
    specs= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    