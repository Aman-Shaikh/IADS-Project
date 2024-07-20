from django.db import models

class RecyclingGuide(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='recycling_guides/')
    description = models.TextField()
    detailed_description = models.TextField()

    def __str__(self):
        return self.title
