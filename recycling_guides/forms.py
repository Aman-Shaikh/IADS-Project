from django import forms
from .models import RecyclingGuide

class RecyclingGuideForm(forms.ModelForm):
    class Meta:
        model = RecyclingGuide
        fields = ['title', 'image', 'description', 'detailed_description']
