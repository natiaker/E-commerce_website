from django import forms
from .models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'categories', 'image', 'stock')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter product name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter product description'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            # 'categories': forms.Select(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
        }
