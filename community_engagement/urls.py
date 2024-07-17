from django.urls import path
from community_engagement import views
from community_engagement.views import CommentCreateView

urlpatterns = [
    path('forum-highlights/', views.HighlightThreadListView, name='highlight_thread_list'),
    path('forum-highlights/new/', views.HighlightThreadCreateView, name='highlight_thread_create'),
    path('forum-highlights/<int:pk>/', views.HighlightThreadDetailView, name='highlight_thread_detail'),
    path('forum-highlights/<int:pk>/comment/', CommentCreateView.as_view(), name='comment_create'),
]
