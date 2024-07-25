from django.contrib import admin
from .models import ServiceRequest

class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'service_type', 'submitted_at')
    search_fields = ('name', 'email', 'service_type')

admin.site.register(ServiceRequest, ServiceRequestAdmin)

