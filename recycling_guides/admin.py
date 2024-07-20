from django.contrib import admin
from django.utils.html import format_html
from .models import RecyclingGuide


class RecyclingGuideAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image_tag')
    search_fields = ('title', 'description')
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.image.url))
        return None

    image_tag.short_description = 'Image'

    fieldsets = (
        (None, {
            'fields': ('title', 'image', 'image_tag', 'description', 'detailed_description')
        }),
    )


admin.site.register(RecyclingGuide, RecyclingGuideAdmin)
