from django import forms
from order.models import CustomerInfo
import re
from django.core.exceptions import ValidationError


# Custom validation function for mobile numbers.
def validate_mobile(value):
    mobile_pattern = re.compile(r'^\d{10}$')
    if not mobile_pattern.match(str(value)):
        raise ValidationError('Mobile number must be 9 digits.')


class OrderForm(forms.ModelForm):
    class Meta:
        model = CustomerInfo
        fields = ['first_name', 'last_name', 'address', 'mobile']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your Firstname'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your Lastname'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your address'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 555123456'}),
        }

    # the clean_mobile method is overridden to apply the custom validation.
    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        validate_mobile(mobile)
        return mobile
