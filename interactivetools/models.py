from django.db import models


class RecyclableItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class CarbonFootprint(models.Model):
    miles_per_week = models.PositiveIntegerField()
    carbon_footprint = models.FloatField()
    category = models.CharField(max_length=50, default='Unknown')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.miles_per_week} miles/week - {self.carbon_footprint} kg CO2/year"