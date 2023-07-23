from django.contrib import admin
from bakeryProject.orders.models import Order


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = ('id', 'user', 'products', 'pickup_time', 'status', 'total_price')
    search_fields = ('id', 'products', 'pickup_time', 'status', 'total_price')
    ordering = ('id', 'user', 'products', 'pickup_time', 'status', 'total_price')
    list_filter = ('id', 'user', 'products', 'pickup_time', 'status', 'total_price')
