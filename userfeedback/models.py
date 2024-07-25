from django.db import models

class Complaint(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    complaint = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.email}'
