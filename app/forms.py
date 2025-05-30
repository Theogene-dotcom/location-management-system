# locations/forms.py
from django import forms
from .models import CustomerLocation

class CustomerLocationForm(forms.ModelForm):
    class Meta:
        model = CustomerLocation
        fields = ['address', 'city', 'country', 'latitude', 'longitude']
        widgets = {
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }
