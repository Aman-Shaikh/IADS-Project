from django.contrib import admin
from .models import RecyclableItem, CarbonFootprint

@admin.register(RecyclableItem)
class RecyclableItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(CarbonFootprint)
class CarbonFootprintAdmin(admin.ModelAdmin):
    list_display = ('miles_per_week', 'carbon_footprint', 'category', 'created_at')
    search_fields = ('miles_per_week', 'carbon_footprint', 'category')
    list_filter = ('category', 'created_at')
    readonly_fields = ('created_at',)
