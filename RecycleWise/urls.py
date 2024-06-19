# recyclewise/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('user/', include('user.urls')),
    path('guides/', include('guides.urls')),
    # path('search/', include('search.urls')),
    # path('contact/', include('contact.urls')),
    # path('recycling-centers/', include('recycling_centers.urls')),
    path('uploads/', include('uploads.urls')),
]
