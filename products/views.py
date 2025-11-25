from django.shortcuts import render,get_object_or_404
from .models import Product
# Create your views here.

def home(request):
    products =Product.objects.all()[:3]
    return render(request,"products/home.html",{"products":products})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html',{'products':products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    images = product.image.all()
    return render(request, 'products/product_detail.html',{
        'product':product,
        'images':images,
        })

