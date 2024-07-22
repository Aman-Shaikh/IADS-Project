from django.urls import path
from . import views

urlpatterns = [
    path('getting_started/', views.getting_started, name='getting_started'),  # Getting Started page
]