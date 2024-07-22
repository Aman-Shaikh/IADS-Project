from django.urls import path
from . import views

urlpatterns = [
    path('', views.featured_videos_list, name='featured_videos_list'),
    path('add/', views.add_featured_video, name='add_featured_video'),
]
