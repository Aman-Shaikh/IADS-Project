from django.urls import path
from . import views

urlpatterns = [
    path('profile_edit/', views.profile_edit, name='profile_edit'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('user_history/', views.user_history, name='user_history'),
    path('user_history_view/', views.user_history_view, name='user_history_view'),
]
