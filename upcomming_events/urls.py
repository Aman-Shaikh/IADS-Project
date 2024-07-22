from django.urls import path
from .views import (
    CommunityCleanUpListView, CommunityCleanUpDetailView, CommunityCleanUpRSVPView, RecyclingWorkshopListView, RecyclingWorkshopDetailView, RecyclingWorkshopRSVPView, WorkshopFeedbackView
)

urlpatterns = [
    path('', CommunityCleanUpListView.as_view(), name='community-cleanup-list'),
    path('community_cleanup/<int:pk>/', CommunityCleanUpDetailView.as_view(), name='community-cleanup-detail'),
    path('community_cleanup/<int:pk>/rsvp/', CommunityCleanUpRSVPView.as_view(), name='community-cleanup-rsvp'),

    path('recycling_workshop/', RecyclingWorkshopListView.as_view(), name='recycling-workshop-list'),
    path('recycling_workshop/<int:pk>/', RecyclingWorkshopDetailView.as_view(), name='recycling-workshop-detail'),
    path('recycling_workshop/<int:pk>/rsvp/', RecyclingWorkshopRSVPView.as_view(), name='recycling-workshop-rsvp'),
    path('recycling_workshop/<int:pk>/feedback/', WorkshopFeedbackView.as_view(), name='workshop-feedback'),
]
