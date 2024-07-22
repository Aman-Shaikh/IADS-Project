from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Review(models.Model):
    SERVICE_CHOICES = [
        ('ES', 'Events Service'),
        ('GS', 'Guidelines Service'),
        ('TS', 'Tips Service'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    feedback = models.TextField(max_length=100)
    review_date = models.DateTimeField(default=timezone.now)
    service = models.CharField(max_length=20, choices=SERVICE_CHOICES, default='ES')

    def __str__(self):
        return f'Review by {self.user.username} for {self.get_service_display()} - {self.rating} Stars'

