from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Event, RSVP
from .forms import (
    CommunityCleanUpForm, CommunityCleanUpRSVPForm, RecyclingWorkshopForm, RecyclingWorkshopRSVPForm
)

# Base views for events
class EventListView(ListView):
    model = Event
    template_name = 'upcoming_events/event_list.html'
    context_object_name = 'events'

class EventDetailView(DetailView):
    model = Event
    template_name = 'upcoming_events/event_detail.html'
    context_object_name = 'event'

class EventCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Event
    template_name = 'upcoming_events/event_form.html'
    success_url = '/upcoming_events/'

    def test_func(self):
        return self.request.user.is_superuser

class RSVPCreateView(LoginRequiredMixin, CreateView):
    model = RSVP
    template_name = 'upcoming_events/rsvp_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.event = get_object_or_404(Event, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return redirect('event-detail', pk=self.kwargs['pk']).url

# Community Clean-Up views
class CommunityCleanUpListView(EventListView):
    queryset = Event.objects.filter(event_type='CCU')
    template_name = 'upcoming_events/community_cleanup_list.html'

class CommunityCleanUpDetailView(EventDetailView):
    template_name = 'upcoming_events/community_cleanup_detail.html'

class CommunityCleanUpCreateView(EventCreateView):
    form_class = CommunityCleanUpForm

class CommunityCleanUpRSVPView(RSVPCreateView):
    form_class = CommunityCleanUpRSVPForm
    template_name = 'upcoming_events/community_cleanup_rsvp_form.html'

# Recycling Workshop views
class RecyclingWorkshopListView(EventListView):
    queryset = Event.objects.filter(event_type='RW')
    template_name = 'upcoming_events/recycling_workshop_list.html'

class RecyclingWorkshopDetailView(EventDetailView):
    template_name = 'upcoming_events/recycling_workshop_detail.html'

class RecyclingWorkshopCreateView(EventCreateView):
    form_class = RecyclingWorkshopForm

class RecyclingWorkshopRSVPView(RSVPCreateView):
    form_class = RecyclingWorkshopRSVPForm
    template_name = 'upcoming_events/recycling_workshop_rsvp_form.html'
