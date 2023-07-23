from django.contrib import admin
from bakeryProject.orders.models import Order


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = ('id', 'user', 'products', 'pickup_time', 'status', 'total_price')
    search_fields = ('id', 'products', 'pickup_time', 'status', 'total_price')
    ordering = ('id', 'user', 'products', 'pickup_time', 'status', 'total_price')
    list_filter = ('id', 'user', 'products', 'pickup_time', 'status', 'total_price')

    actions = ['update_status_to_ready', 'update_status_to_done']

    def update_status_to_ready(self, request, queryset):
        queryset.update(status='ready_to_pickup')

    update_status_to_ready.short_description = "Mark selected orders as 'Ready to Pickup'"

    def update_status_to_done(self, request, queryset):
        queryset.update(status='done')

    update_status_to_done.short_description = "Mark selected orders as 'Done'"
