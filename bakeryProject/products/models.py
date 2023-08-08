from django.db import models


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('salty', 'Salty'),
        ('sweet', 'Sweet'),
        ('drinks', 'Drinks'),
    ]

    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    currency = models.CharField(max_length=5, default='€')
    picture_url = models.URLField()
    description = models.TextField(blank=True, null=True, default='Detailed description of the product')
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name

