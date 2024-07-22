from django.urls import path
from community_engagement import views

from community_engagement.views import CommentCreateView

urlpatterns = [
    path('forum-highlights/', views.HighlightThreadListView, name='highlight_thread_list'),
    path('forum-highlights/new/', views.HighlightThreadCreateView, name='highlight_thread_create'),
    path('forum-highlights/<int:pk>/', views.HighlightThreadDetailView, name='highlight_thread_detail'),
    path('forum-highlights/<int:pk>/comment/', CommentCreateView.as_view(), name='comment_create'),

    # User Stories URLs
    path('user-stories/', views.UserStoryListView, name='user_story_list'),
    path('user-stories/new/', views.UserStoryCreateView, name='user_story_create'),
    path('user-stories/<int:pk>/', views.UserStoryDetailView, name='user_story_detail'),
    path('user-stories/<int:pk>/edit/', views.UserStoryUpdateView, name='user_story_edit'),
    path('user-stories/<int:pk>/comment/', views.StoryCommentCreateView, name='story_comment_create'),

]
