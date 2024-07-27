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

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if RecyclableItem.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError("An item with this name already exists.")
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 10:
            raise forms.ValidationError("The description must be at least 10 characters long.")
        return description
