# Generated by Django 5.0.6 on 2024-06-19 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_remove_cart_quantity_alter_cartitem_quantity'),
        ('shop', '0004_delete_cart'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together={('cart', 'product')},
        ),
    ]