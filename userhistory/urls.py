from django.urls import path
from . import views

urlpatterns = [
    path('user-history/', views.user_history, name='user_history')
]
