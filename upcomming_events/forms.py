from django import forms
from .models import RSVP, CommunityCleanUpRSVP, RecyclingWorkshopRSVP, WorkshopFeedback

class CommunityCleanUpRSVPForm(forms.ModelForm):
    class Meta:
        model = RSVP
        fields = ['number_of_participants', 'additional_supplies']

class CommunityCleanUpForm(forms.ModelForm):
    class Meta:
        model = CommunityCleanUpRSVP
        fields = ['name', 'phone_number', 'email_id', 'gender']


class RecyclingWorkshopRSVPForm(forms.ModelForm):
    class Meta:
        model = RecyclingWorkshopRSVP
        fields = ['name', 'phone_number', 'email_id', 'gender']

class WorkshopFeedbackForm(forms.ModelForm):
    class Meta:
        model = WorkshopFeedback
        fields = ['rating', 'comments']