# infographics/models.py

from django.db import models

class Infographic(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='infographics/')
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

