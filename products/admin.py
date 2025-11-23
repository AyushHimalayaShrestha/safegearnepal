from django.contrib import admin
from .models import Product, ProductImage
# Register your models here.
class ProductImageInLine(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display =('name','category','price', 'created_at')
    list_filter = ('category','created_at')
    search_fields = ('name','description')
    inlines = [ProductImageInLine]