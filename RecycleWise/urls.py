# recyclewise/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('', include('getting_started.urls')),
    path('upcoming_events/', include('upcoming_events.urls')),
    # path('', include('userfeedback.urls')),
    path('interactivetools/', include('interactivetools.urls')),

]
