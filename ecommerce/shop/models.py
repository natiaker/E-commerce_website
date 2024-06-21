from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categories'


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    categories = models.ManyToManyField(Category)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products_pictures/', default='default/default-product-image.png', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product'


