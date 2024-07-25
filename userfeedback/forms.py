from django import forms
from .models import Complaint

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['name', 'email', 'phone', 'complaint']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First and Last'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@domain.tld'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(555) 555-5555'}),
            'complaint': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your Complaint here.....', 'rows': 6}),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone and not phone.isdigit():
            raise forms.ValidationError("Phone number must contain only digits.")
        return phone
