from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    picture_url = models.URLField()

    def __str__(self):
        return self.name

