from django.contrib import admin
from bakeryProject.orders.models import Order


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    pass
