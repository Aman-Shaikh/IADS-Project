from django import forms
from .models import RecyclableItem

class RecyclableItemForm(forms.ModelForm):
    class Meta:
        model = RecyclableItem
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter item name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter item description'}),
        }
        labels = {
            'name': 'Item Name',
            'description': 'Description',
        }
