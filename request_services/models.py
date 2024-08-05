from django.db import models
from django.contrib.auth.models import User

class ServiceRequest(models.Model):
    SERVICE_CHOICES = [
        ('Collect Recyclable Materials', 'Collect Recyclable Materials'),
        # Add more service types here
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # No default, ensures user association
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField()
    service_type = models.CharField(max_length=100, choices=SERVICE_CHOICES)
    request_details = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.service_type}"
