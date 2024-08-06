from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Event, CommunityCleanUpRSVP, RecyclingWorkshopRSVP, WorkshopMaterial
from .forms import CommunityCleanUpForm, RecyclingWorkshopRSVPForm

# Community Cleanup List View
def community_cleanup_list(request):
    events = Event.objects.filter(event_type='CCU')
    return render(request, 'upcomming_events/community_cleanup_list.html', {'events': events})

# Community Cleanup Detail View
def community_cleanup_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'upcomming_events/community_cleanup_detail.html', {'event': event})

# Community Cleanup RSVP View
@login_required
def community_cleanup_rsvp(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = CommunityCleanUpForm(request.POST)
        if form.is_valid():
            rsvp = form.save(commit=False)
            rsvp.event = event
            rsvp.user = request.user  # Set the user here
            rsvp.save()
            return redirect('community-cleanup-detail', pk=event.pk)
    else:
        form = CommunityCleanUpForm()
    return render(request, 'upcomming_events/community_cleanup_rsvp_form.html', {'form': form, 'event': event})

# Recycling Workshop List View
def recycling_workshop_list(request):
    events = Event.objects.filter(event_type='RW')
    return render(request, 'upcomming_events/recycling_workshop_list.html', {'events': events})

# Recycling Workshop Detail View
def recycling_workshop_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'upcomming_events/recycling_workshop_detail.html', {'event': event})

# Recycling Workshop RSVP View
@login_required
def recycling_workshop_rsvp(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = RecyclingWorkshopRSVPForm(request.POST)
        if form.is_valid():
            rsvp = form.save(commit=False)
            rsvp.event = event
            rsvp.user = request.user
            rsvp.save()
            return redirect('recycling-workshop-detail', pk=event.pk)
    else:
        form = RecyclingWorkshopRSVPForm()
    return render(request, 'upcomming_events/recycling_workshop_rsvp_form.html', {'form': form, 'event': event})

@login_required
def community_cleanup_registrations_view(request):
    user = request.user
    registrations = CommunityCleanUpRSVP.objects.filter(user=user)
    print(len(registrations))
    return render(request, 'upcomming_events/community_cleanup_registrations.html', {'registrations': registrations})

@login_required
def recycling_workshop_registrations_view(request):
    user = request.user
    registrations = RecyclingWorkshopRSVP.objects.filter(user=user)
    print(len(registrations))
    return render(request, 'upcomming_events/recycling_workshop_registrations.html', {'registrations': registrations})