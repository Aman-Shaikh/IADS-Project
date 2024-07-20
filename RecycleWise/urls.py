# recyclewise/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('', include('getting_started.urls')),
    path('', include('quicktips.urls')),
    path('', include('reviews.urls')),
    path('', include('user_profile.urls')),
    path('upcoming_events/', include('upcomming_events.urls')),
    path('', include('userfeedback.urls')),
    path('interactivetools/', include('interactivetools.urls')),
    path('community_engagement/', include('community_engagement.urls')),
    path('recycling_guides/', include('recycling_guides.urls')),
]
