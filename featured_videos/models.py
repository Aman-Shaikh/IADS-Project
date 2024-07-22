from django.db import models

class FeaturedVideo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_url = models.URLField()
    thumbnail = models.ImageField(upload_to='thumbnails/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
