# infographics/forms.py

from django import forms
from .models import Infographic

class InfographicForm(forms.ModelForm):
    class Meta:
        model = Infographic
        fields = ['title', 'description', 'image']
