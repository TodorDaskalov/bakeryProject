from django.contrib.auth import get_user_model
from django.db import models

from bakeryProject.products.models import Product


class Order(models.Model):
    STATUS_CHOICES = (
        ('received', 'Received'),
        ('working', 'Working on it'),
        ('ready_to_pickup', 'Ready to pickup'),
        ('done', 'Done'),
    )

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    products = models.CharField(max_length=500)
    pickup_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    total_price = models.FloatField()

    def __str__(self):
        return f"Order #{self.pk} - {self.user}"

