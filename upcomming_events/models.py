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
# class RSVP(models.Model):
#     event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='rsvps')
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     number_of_participants = models.PositiveIntegerField(default=1)
#     additional_supplies = models.TextField(blank=True, null=True)
#
#     def __str__(self):
#         return f"{self.user.username} - {self.event.title}"

# class CommunityCleanUpRSVP(models.Model):
#     GENDER_CHOICES = [
#         ('M', 'Male'),
#         ('F', 'Female'),
#         ('O', 'Other'),
#     ]
#
#     event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='community_clean_up_rsvps')
#     name = models.CharField(max_length=255)
#     phone_number = models.CharField(max_length=15)
#     email_id = models.EmailField()
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
#
#     def __str__(self):
#         return f"{self.name} - {self.event.title}"
#
# class RecyclingWorkshopRSVP(models.Model):
#     GENDER_CHOICES = [
#         ('M', 'Male'),
#         ('F', 'Female'),
#         ('O', 'Other'),
#     ]
#
#     event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='recycling_workshop_rsvps')
#     name = models.CharField(max_length=255)
#     phone_number = models.CharField(max_length=15)
#     email_id = models.EmailField()
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
#
#     def __str__(self):
#         return f"{self.name} - {self.event.title}"

# Community Clean-Up RSVP model
class CommunityCleanUpRSVP(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='community_clean_up_rsvps')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email_id = models.EmailField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return f"{self.name} - {self.event.title}"

# Recycling Workshop RSVP model
class RecyclingWorkshopRSVP(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='recycling_workshop_rsvps')
    user = models.ForeignKey(User, on_delete=models.CASCADE,  null=True, blank=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email_id = models.EmailField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return f"{self.name} - {self.event.title}"

class WorkshopMaterial(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='materials')
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='workshop_materials/')

    def __str__(self):
        return self.title

# class WorkshopFeedback(models.Model):
#     event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='feedbacks')
#     user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#     rating = models.PositiveSmallIntegerField()
#     comments = models.TextField()
#
#     def __str__(self):
#    return f"{self.user.username} - {self.event.title}"