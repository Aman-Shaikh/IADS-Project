from django import forms

from .models import HighlightThread, Comment, UserStory, StoryComment


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


class UserStoryForm(forms.ModelForm):
    class Meta:
        model = UserStory
        fields = ['title', 'content', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter story title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Enter the full content'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

class StoryCommentForm(forms.ModelForm):
    class Meta:
        model = StoryComment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter your comment'}),
        }

