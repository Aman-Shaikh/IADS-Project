from django.contrib import admin
from .models import Event, RSVP, CommunityCleanUpRSVP, RecyclingWorkshopRSVP, WorkshopMaterial, WorkshopFeedback


# Register your models here.
admin.site.register(Event)
admin.site.register(RSVP)
admin.site.register(CommunityCleanUpRSVP)
admin.site.register(RecyclingWorkshopRSVP)
admin.site.register(WorkshopMaterial)
admin.site.register(WorkshopFeedback)