from django.urls import path
from .views import request_service_view,service_requests_view

urlpatterns = [
    path('request_service/', request_service_view, name='request_service'),
    path('request_service/my-service-requests/', service_requests_view, name='service_requests_view'),
]
