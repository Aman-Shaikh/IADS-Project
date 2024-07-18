from django import forms
from .models import Tip, WasteType

class WasteTypeForm(forms.ModelForm):
    class Meta:
        model = WasteType
        fields = ['waste_choices']

class TipForm(forms.ModelForm):
    class Meta:
        model = Tip
        fields = ['waste_type', 'description']
        widgets = {
            'waste_type': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
