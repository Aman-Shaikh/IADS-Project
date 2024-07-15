from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class HighlightThread(models.Model):
    title = models.CharField(max_length=200)
    snippet = models.TextField()
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    thread = models.ForeignKey(HighlightThread, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)