# Generated by Django 5.0.6 on 2024-06-20 14:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_orderform'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='info',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='order.orderform'),
        ),
    ]
