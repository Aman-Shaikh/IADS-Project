# recyclewise/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('', include('getting_started.urls')),
<<<<<<< HEAD
    path('', include('quicktips.urls')),
    path('', include('reviews.urls')),
    # path('', include('userfeedback.urls')),
=======
    path('upcoming_events/', include('upcomming_events.urls')),
    path('', include('userfeedback.urls')),
    path('interactivetools/', include('interactivetools.urls')),
    path('community_engagement/', include('community_engagement.urls')),
>>>>>>> 8d955489be6f7a659d2408d5c8e0460bf5efc0fc
]
