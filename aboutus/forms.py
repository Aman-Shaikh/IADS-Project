from django import forms
from django.contrib.auth.models import User  # Import User model
from .models import TeamMember,Section

class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['name', 'description', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'})
        }


class TeamMemberForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )

    class Meta:
        model = TeamMember
        fields = ['user', 'bio', 'sections', 'image']  # Include the user field
        widgets = {
            'sections': forms.CheckboxSelectMultiple(),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

