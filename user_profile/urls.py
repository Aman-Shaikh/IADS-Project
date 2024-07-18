from django.urls import path
from .views import profile,profile_update

urlpatterns = [
    # other url patterns
    path('profile/', profile, name='profile'),
    path('profile/update/', profile_update, name='profile_update'),
]
