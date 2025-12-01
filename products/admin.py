from django.contrib import admin
from .models import Product, Tender, Inquiry, Category, ProductImage
# Supplier removed - no longer needed

# Register your models here.

# Category Admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price_npr', 'stock', 'created_at')  # Added stock
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'description')


# SupplierAdmin REMOVED - No longer needed


@admin.register(Tender)
class TenderAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_date', 'end_date')
    search_fields = ('title',)


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'product', 'created_at')
    search_fields = ('name', 'email', 'phone')


# ProductImage Admin
@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')


# Customize admin site headers
admin.site.site_header = "Himalaya Road Safety Admin"
admin.site.site_title = "Himalaya Road Safety Admin Portal"
admin.site.index_title = "Welcome to Himalaya Road Safety Admin"