from django.urls import path
from .views import request_service_view

urlpatterns = [
    path('request_service/', request_service_view, name='request_service'),
]
