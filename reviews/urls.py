from django.urls import path
from .views import get_reviews

urlpatterns = [
    path('reviews/', get_reviews, name='get_reviews'),
]
