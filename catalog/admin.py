from django.contrib import admin
from catalog.models import Product, Category

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'price', 'product_category', "preview_image", 'description')
    search_fields = ('title',)
    list_filter = ('product_category',)
    fields = ("description",)
    readonly_fields = ('creation_date', 'change_date',)

@admin.register(Category)
class CategorytAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title',)
