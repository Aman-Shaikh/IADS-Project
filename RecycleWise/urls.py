# recyclewise/urls.py

from django.contrib import admin

from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('', include('getting_started.urls')),
    path('', include('quicktips.urls')),
    path('', include('reviews.urls')),
    path('', include('user_profile.urls')),
    path('', include('userfeedback.urls')),
    path('', include('request_services.urls')),
    path('upcoming_events/', include('upcomming_events.urls')),
    path('infographics/', include('infographics.urls')),
    path('interactivetools/', include('interactivetools.urls')),
    path('community_engagement/', include('community_engagement.urls')),
    path('recycling_guides/', include('recycling_guides.urls')),
    path('userhistory/', include('userhistory.urls')),
    path('featured_videos/', include('featured_videos.urls')),
    path('aboutus/', include('aboutus.urls')),


    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

