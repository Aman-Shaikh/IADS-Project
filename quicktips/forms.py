from django import forms
from .models import WasteType


class WasteTypeForm(forms.ModelForm):
    class Meta:
        model = WasteType
        fields = ['waste_choices']
