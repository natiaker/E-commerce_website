# Generated by Django 5.0.6 on 2024-06-20 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_product_price_alter_product_stock'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]
