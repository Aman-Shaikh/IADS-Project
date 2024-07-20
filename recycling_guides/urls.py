from django.urls import path
from . import views

urlpatterns = [
    path('', views.recycling_guides_list, name='recycling_guides_list'),
    path('<int:pk>/', views.recycling_guide_detail, name='recycling_guide_detail'),
    path('add/', views.add_recycling_guide, name='add_recycling_guide'),
]
