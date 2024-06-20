# user/urls.py

from django.urls import path
from .views import profile_edit, ForgotPasswordView, user_history, logout
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('profile_edit/', profile_edit, name='profile_edit'),
    path('forgot_password/', ForgotPasswordView.as_view(), name='forgot_password'),
    path('user_history/', user_history, name='user_history'),
    path('logout/', logout, name='logout'),
]
