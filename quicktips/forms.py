from django import forms
from .models import QuickTip

class QuickTipForm(forms.ModelForm):
    class Meta:
        model = QuickTip
        fields = ['waste_choices']
