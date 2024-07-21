from django.contrib import admin
from .models import HighlightThread, Comment, UserStory, StoryComment, Category

# Register your models here.
admin.site.register(HighlightThread)
admin.site.register(Comment)
admin.site.register(UserStory)
admin.site.register(StoryComment)
admin.site.register(Category)
