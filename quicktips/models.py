from django.db import models


# Create your models here.
class QuickTip(models.Model):
    Waste_Options = [
        ('BW', 'Bulky Waste'),
        ('GW', 'General Waste'),
        ('HW', 'Hazardous Waste'),
        ('OW', 'Organic Waste'),
        ('RW', 'Recyclable Waste'),
        ('SW', 'Select your Waste')
    ]
    waste_choices = models.CharField(max_length=2, choices=Waste_Options, default='SW')

    def __str__(self):
        return self.waste_choices


class Tips(models.Model):
    waste_type = models.ForeignKey(QuickTip, related_name='Tips', on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    # image = models.ImageField(upload_to='Waste-Images/', null=True, blank=True)

    def __str__(self):
        return f"{self.description}"
