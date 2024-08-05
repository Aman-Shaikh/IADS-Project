from django import forms
from .models import CommunityCleanUpRSVP, RecyclingWorkshopRSVP

class CommunityCleanUpForm(forms.ModelForm):
    class Meta:
        model = CommunityCleanUpRSVP
        fields = ['name', 'phone_number', 'email_id', 'gender']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name.isalpha():
            raise forms.ValidationError("Name should only contain letters.")
        return name

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number.isdigit():
            raise forms.ValidationError("Phone number should only contain digits.")
        return phone_number

class RecyclingWorkshopRSVPForm(forms.ModelForm):
    class Meta:
        model = RecyclingWorkshopRSVP
        fields = ['name', 'phone_number', 'email_id', 'gender']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name.isalpha():
            raise forms.ValidationError("Name should only contain letters.")
        return name

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number.isdigit():
            raise forms.ValidationError("Phone number should only contain digits.")
        return phone_number
