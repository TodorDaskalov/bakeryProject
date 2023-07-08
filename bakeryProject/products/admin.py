from django.contrib import admin
from bakeryProject.products.models import Product


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    pass
