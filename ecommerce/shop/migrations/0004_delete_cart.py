# Generated by Django 5.0.6 on 2024-06-18 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_product_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]