from django.urls import path
from bakeryProject.orders.views import show_orders, update_order, custom_order

urlpatterns = [
    path('orders_in_process/', show_orders, name='show_orders'),
    path('update_order/<int:pk>', update_order, name='update_order'),
    path('custom_order/', custom_order, name='custom_order'),
]
