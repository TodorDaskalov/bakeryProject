from django.contrib import admin
from bakeryProject.products.models import Product


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    list_filter = ('name', 'price', 'category')
    search_fields = ('name', 'price', 'category')
    ordering = ('name', 'price', 'category')
