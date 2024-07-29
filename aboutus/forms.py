from django import forms
from .models import TeamMember, Section

class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['name', 'description']

class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ['bio', 'sections']
        widgets = {
            'sections': forms.CheckboxSelectMultiple(),
        }
