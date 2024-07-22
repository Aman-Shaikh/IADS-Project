from django.urls import path
from . import views

urlpatterns = [
    path('usercomplaint/', views.user_complaint_view, name='usercomplaint'),
]
