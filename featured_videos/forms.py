from django import forms
from .models import FeaturedVideo

class FeaturedVideoForm(forms.ModelForm):
    class Meta:
        model = FeaturedVideo
        fields = ['title', 'description', 'video_url', 'thumbnail']
