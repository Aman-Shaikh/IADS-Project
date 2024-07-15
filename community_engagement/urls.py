from django.urls import path
from .views import HighlightThreadListView, HighlightThreadDetailView, HighlightThreadCreateView, CommentCreateView

urlpatterns = [
    path('forum-highlights/', HighlightThreadListView.as_view(), name='highlight_thread_list'),
    path('forum-highlights/<int:pk>/', HighlightThreadDetailView.as_view(), name='highlight_thread_detail'),
    path('forum-highlights/new/', HighlightThreadCreateView.as_view(), name='highlight_thread_create'),
    path('forum-highlights/<int:pk>/comment/', CommentCreateView.as_view(), name='comment_create'),
]
