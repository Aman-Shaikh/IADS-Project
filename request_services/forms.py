from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['name', 'email', 'phone', 'address', 'service_type', 'request_details']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Address', 'rows': 3}),
            'service_type': forms.Select(attrs={'class': 'form-control'}),
            'request_details': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Request Details', 'rows': 6}),
        }
