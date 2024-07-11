# user_feedback/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('userfeedback/', views.user_feedback, name='userfeedback'),  # User Feedback page
]
