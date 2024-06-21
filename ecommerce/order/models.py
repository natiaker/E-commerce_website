from django.db import models
from django.contrib.auth.models import User
from cart.models import Cart
from shop.models import Product


class CustomerInfo(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.TextField()
    mobile = models.CharField(max_length=13)

    class Meta:
        db_table = 'order_form'

    def __str__(self):
        return f'{self.first_name} {self.last_name} Form Info'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    customer_info = models.OneToOneField(CustomerInfo, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'order'

    def __str__(self):
        return f'{self.user.name}\'s Order'

    def total_price(self):
        total = sum(item.get_total_price() for item in self.order_items.all())
        return total


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    class Meta:
        db_table = 'order_item'
        unique_together = ('order', 'product')

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'

    def get_total_price(self):
        return self.quantity * self.product.price