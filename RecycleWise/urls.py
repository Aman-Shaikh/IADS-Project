# recyclewise/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('', include('getting_started.urls')),
    # path('', include('userfeedback.urls')),
    path('interactivetools/', include('interactivetools.urls')),
]
