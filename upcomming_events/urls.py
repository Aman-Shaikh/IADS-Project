from django.urls import path
from .views import (
    CommunityCleanUpListView, CommunityCleanUpDetailView, CommunityCleanUpCreateView, CommunityCleanUpRSVPView,
    RecyclingWorkshopListView, RecyclingWorkshopDetailView, RecyclingWorkshopCreateView, RecyclingWorkshopRSVPView,
    EventListView, EventDetailView, EventCreateView, RSVPCreateView
)

urlpatterns = [
    path('', EventListView.as_view(), name='event-list'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('event/new/', EventCreateView.as_view(), name='event-create'),
    path('event/<int:pk>/rsvp/', RSVPCreateView.as_view(), name='rsvp-create'),

    path('community_cleanup/', CommunityCleanUpListView.as_view(), name='community-cleanup-list'),
    path('community_cleanup/<int:pk>/', CommunityCleanUpDetailView.as_view(), name='community-cleanup-detail'),
    path('community_cleanup/new/', CommunityCleanUpCreateView.as_view(), name='community-cleanup-create'),
    path('community_cleanup/<int:pk>/rsvp/', CommunityCleanUpRSVPView.as_view(), name='community-cleanup-rsvp'),

    path('recycling_workshop/', RecyclingWorkshopListView.as_view(), name='recycling-workshop-list'),
    path('recycling_workshop/<int:pk>/', RecyclingWorkshopDetailView.as_view(), name='recycling-workshop-detail'),
    path('recycling_workshop/new/', RecyclingWorkshopCreateView.as_view(), name='recycling-workshop-create'),
    path('recycling_workshop/<int:pk>/rsvp/', RecyclingWorkshopRSVPView.as_view(), name='recycling-workshop-rsvp'),
]
