from django.contrib import admin
from .models import TeamMember, Section

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')
    fields = ('user', 'bio', 'image', 'sections')  # Include the image field

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
