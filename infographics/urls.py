# infographics/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.infographic_list, name='infographic_list'),
    path('infographic/<int:pk>/', views.infographic_detail, name='infographic_detail'),
    path('infographic/new/', views.infographic_new, name='infographic_new'),
    path('infographic/<int:pk>/edit/', views.infographic_edit, name='infographic_edit'),
]
