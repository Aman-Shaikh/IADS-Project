# recyclewise/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('', include('getting_started.urls')),
    path('', include('quicktips.urls')),
    path('', include('reviews.urls')),
    # path('', include('userfeedback.urls')),
]
