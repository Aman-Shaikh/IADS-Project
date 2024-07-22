from django.urls import path
from community_engagement import views
from community_engagement.views import CommentCreateView, UserStoryListView, UserStoryCreateView, UserStoryDetailView, \
    UserStoryUpdateView, StoryCommentCreateView

urlpatterns = [
    path('forum-highlights/', views.HighlightThreadListView, name='highlight_thread_list'),
    path('forum-highlights/new/', views.HighlightThreadCreateView, name='highlight_thread_create'),
    path('forum-highlights/<int:pk>/', views.HighlightThreadDetailView, name='highlight_thread_detail'),
    path('forum-highlights/<int:pk>/comment/', CommentCreateView.as_view(), name='comment_create'),

    # User Stories URLs
    path('user-stories/', UserStoryListView.as_view(), name='user_story_list'),
    path('user-stories/new/', UserStoryCreateView.as_view(), name='user_story_create'),
    path('user-stories/<int:pk>/', UserStoryDetailView.as_view(), name='user_story_detail'),
    path('user-stories/<int:pk>/edit/', UserStoryUpdateView.as_view(), name='user_story_edit'),
    path('user-stories/<int:pk>/comment/', StoryCommentCreateView.as_view(), name='story_comment_create'),


]
