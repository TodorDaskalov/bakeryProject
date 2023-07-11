from django.urls import path
from bakeryProject.cart.views import AddToCartView, cart_view, RemoveItemView, order_products

urlpatterns = [
    path('', cart_view, name='cart_page'),
    path('add_to_cart/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/remove_item/<int:pk>/', RemoveItemView.as_view(), name='remove_item'),
    path('cart/order', order_products, name='order_products'),
]
