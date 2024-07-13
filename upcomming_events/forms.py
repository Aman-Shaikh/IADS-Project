from django import forms
from .models import Event, RSVP

# Base form for creating or editing events
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'time', 'location', 'organizer', 'contact_email']

# Form for creating or editing a community clean-up event
class CommunityCleanUpForm(EventForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.event_type = 'CCU'

# Form for creating or editing a recycling workshop event
class RecyclingWorkshopForm(EventForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.event_type = 'RW'

# Base form for RSVPing to an event
class RSVPForm(forms.ModelForm):
    class Meta:
        model = RSVP
        fields = ['number_of_participants', 'additional_supplies']

# Form for users to RSVP to a community clean-up event
class CommunityCleanUpRSVPForm(RSVPForm):
    pass

# Form for users to RSVP to a recycling workshop event
class RecyclingWorkshopRSVPForm(RSVPForm):
    pass
