from django.contrib import admin
from .models import Product,ProductImage,Supplier,Tender,Inquiry
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

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display =('name','contact_person','phone','email','created_at')
    search_fields =('name','contact_person')


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display =('product','image')

@admin.register(Tender)
class TenderAdmin(admin.ModelAdmin):
    list_display = ('title','publish_date','end_date')
    search_fields = ('title')

@admin.register(Inquiry)
class TenderAdmin(admin.ModelAdmin):
    list_display =('name','email','phone','product','created_at')
    search_fields = ('name','email','phone')