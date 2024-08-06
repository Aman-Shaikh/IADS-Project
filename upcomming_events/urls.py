from django.urls import path
from .views import (
    community_cleanup_list,
    community_cleanup_detail,
    community_cleanup_rsvp,
    recycling_workshop_list,
    recycling_workshop_detail,
    recycling_workshop_rsvp,
    community_cleanup_registrations_view,
    recycling_workshop_registrations_view,

)
from user_profile.views import profile

urlpatterns = [
    path('', community_cleanup_list, name='community-cleanup-list'),
    path('community_cleanup/<int:pk>/', community_cleanup_detail, name='community-cleanup-detail'),
    path('community_cleanup/<int:pk>/rsvp/', community_cleanup_rsvp, name='community-cleanup-rsvp'),

    path('recycling_workshop/', recycling_workshop_list, name='recycling-workshop-list'),
    path('recycling_workshop/<int:pk>/', recycling_workshop_detail, name='recycling-workshop-detail'),
    path('recycling_workshop/<int:pk>/rsvp/', recycling_workshop_rsvp, name='recycling-workshop-rsvp'),
    # path('recycling_workshop/<int:pk>/feedback/', workshop_feedback, name='workshop-feedback'),
    path('profile/', profile, name='profile'),
    path('profile/community_cleanup_registrations/', community_cleanup_registrations_view,name='community_cleanup_registrations'),
    path('profile/recycling_workshop_registrations/', recycling_workshop_registrations_view,name='recycling_workshop_registrations'),
]
