from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Event, RSVP, CommunityCleanUpRSVP, RecyclingWorkshopRSVP, WorkshopMaterial, WorkshopFeedback
from .forms import CommunityCleanUpForm, RecyclingWorkshopRSVPForm, WorkshopFeedbackForm



class CommunityCleanUpListView(ListView):
    model = Event
    template_name = 'upcomming_events/community_cleanup_list.html'
    context_object_name = 'events'
    queryset = Event.objects.filter(event_type='CCU')

class CommunityCleanUpDetailView(DetailView):
    model = Event
    template_name = 'upcomming_events/community_cleanup_detail.html'
    context_object_name = 'event'

class CommunityCleanUpRSVPView(LoginRequiredMixin, CreateView):
    model = CommunityCleanUpRSVP
    form_class = CommunityCleanUpForm
    template_name = 'upcomming_events/community_cleanup_rsvp_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event'] = get_object_or_404(Event, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.event = get_object_or_404(Event, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return redirect('community-cleanup-detail', pk=self.kwargs['pk']).url


# worskshop views

class RecyclingWorkshopListView(ListView):
    model = Event
    template_name = 'upcomming_events/recycling_workshop_list.html'
    context_object_name = 'events'
    queryset = Event.objects.filter(event_type='RW')

class RecyclingWorkshopDetailView(DetailView):
    model = Event
    template_name = 'upcomming_events/recycling_workshop_detail.html'
    context_object_name = 'event'

class RecyclingWorkshopRSVPView(LoginRequiredMixin, CreateView):
    model = RecyclingWorkshopRSVP
    form_class = RecyclingWorkshopRSVPForm
    template_name = 'upcomming_events/recycling_workshop_rsvp_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event'] = get_object_or_404(Event, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.event = get_object_or_404(Event, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return redirect('recycling-workshop-detail', pk=self.kwargs['pk']).url

class WorkshopFeedbackView(LoginRequiredMixin, CreateView):
    model = WorkshopFeedback
    form_class = WorkshopFeedbackForm
    template_name = 'upcomming_events/workshop_feedback_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event'] = get_object_or_404(Event, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.event = get_object_or_404(Event, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return redirect('recycling-workshop-detail', pk=self.kwargs['pk']).url

class UserRegisteredEventsView(LoginRequiredMixin, ListView):
    template_name = 'upcomming_events/user_registered_events.html'
    context_object_name = 'registered_events'

    def get_queryset(self):
        # Get all RSVP objects where the user is the current logged-in user
        community_cleanups = CommunityCleanUpRSVP.objects.filter(email_id=self.request.user.email)
        recycling_workshops = RecyclingWorkshopRSVP.objects.filter(email_id=self.request.user.email)
        return {
            'community_cleanups': community_cleanups,
            'recycling_workshops': recycling_workshops
        }