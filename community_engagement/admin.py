from django.contrib import admin
from .models import HighlightThread, Comment

# Register your models here.
admin.site.register(HighlightThread)
admin.site.register(Comment)
