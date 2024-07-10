from django.db import models
from django.contrib.auth.models import User

# Event model
class Event(models.Model):
    EVENT_TYPE_CHOICES = [
        ('CCU', 'Community Clean-Up'),
        ('RW', 'Recycling Workshop'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    event_type = models.CharField(max_length=3, choices=EVENT_TYPE_CHOICES)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    organizer = models.CharField(max_length=100)
    contact_email = models.EmailField()

    def __str__(self):
        return self.title

# RSVP model
class RSVP(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='rsvps')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number_of_participants = models.PositiveIntegerField(default=1)
    additional_supplies = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.event.title}"
