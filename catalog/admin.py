from django.contrib import admin
from catalog.models import Product, Category
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'price', 'product_category')
    search_fields = ('title', 'description')
    list_filter = ('product_category',)

@admin.register(Category)
class CategorytAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title',)
