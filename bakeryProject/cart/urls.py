from django.urls import path
from bakeryProject.cart.views import AddToCartView, cart_view


urlpatterns = [
    path('', cart_view, name='cart_page'),
    path('add_to_cart/', AddToCartView.as_view(), name='add_to_cart'),
]
