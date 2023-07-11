from django.db import models
from django.contrib.auth import get_user_model
from bakeryProject.products.models import Product

User = get_user_model()


class Cart(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart for {self.user}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.product.name} - Quantity: {self.quantity}'

