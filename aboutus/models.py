from django.db import models
from django.contrib.auth.models import User

class Section(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class TeamMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    image = models.ImageField(upload_to='team_members/', blank=True, null=True)  # New field
    sections = models.ManyToManyField(Section, related_name='team_members')

    def __str__(self):
        return self.user.username
