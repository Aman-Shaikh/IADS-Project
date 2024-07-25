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

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name.replace(' ', '').isalpha():
            raise forms.ValidationError("Name must only contain letters and spaces.")
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email is required.")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone:
            if not phone.isdigit():
                raise forms.ValidationError("Phone number must be numeric.")
            if len(phone) < 10:
                raise forms.ValidationError("Phone number must be at least 10 digits long.")
        return phone

    def clean_address(self):
        address = self.cleaned_data.get('address')
        if not address:
            raise forms.ValidationError("Address is required.")
        return address

    def clean_service_type(self):
        service_type = self.cleaned_data.get('service_type')
        if service_type not in dict(ServiceRequest.SERVICE_CHOICES).keys():
            raise forms.ValidationError("Invalid service type selected.")
        return service_type

    def clean_request_details(self):
        request_details = self.cleaned_data.get('request_details')
        if not request_details:
            raise forms.ValidationError("Request details are required.")
        return request_details
