from django.urls import path
from . import views

urlpatterns = [
    path('team/', views.team_member_list, name='team_member_list'),
    path('team/<int:pk>/', views.team_member_detail, name='team_member_detail'),
    path('team/add/', views.add_team_member, name='add_team_member'),
    path('team/<int:pk>/edit/', views.edit_team_member, name='edit_team_member'),
    path('sections/', views.section_list, name='section_list'),
    path('sections/<int:pk>/', views.section_detail, name='section_detail'),
    path('sections/add/', views.add_section, name='add_section'),
]
