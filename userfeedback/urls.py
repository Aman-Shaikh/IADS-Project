from django.urls import path
from . import views

urlpatterns = [
    path('userfeedback/', views.user_feedback_view, name='userfeedback'),
]