# Generated by Django 5.0.6 on 2024-06-20 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('mobile', models.CharField(max_length=13)),
            ],
            options={
                'db_table': 'order_form',
            },
        ),
    ]