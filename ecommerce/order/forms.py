from django import forms
from order.models import CustomerInfo


class OrderForm(forms.ModelForm):
    class Meta:
        model = CustomerInfo
        fields = ['first_name', 'last_name', 'address', 'mobile']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your Firstname'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your Lastname'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your address'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 555123456'}),
        }
