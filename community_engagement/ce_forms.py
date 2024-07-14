from django import forms
from .models import HighlightThread, Comment

class HighlightThreadForm(forms.ModelForm):
    class Meta:
        model = HighlightThread
        fields = ['title', 'snippet', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
