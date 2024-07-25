from django.contrib import admin
from .models import Complaint

class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'complaint')
    search_fields = ('name', 'email', 'complaint')

admin.site.register(Complaint, ComplaintAdmin)
