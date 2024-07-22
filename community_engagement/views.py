from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import HighlightThread, Comment, UserStory, StoryComment
from .forms import HighlightThreadForm, CommentForm, UserStoryForm, StoryCommentForm
from django.urls import reverse, reverse_lazy

from django.contrib import messages

def HighlightThreadListView(request):
    threads = HighlightThread.objects.all()
    return render(request, 'community_engagement/highlight_thread_list.html', {'threads': threads})


@login_required
def HighlightThreadCreateView(request):
    if request.method == 'POST':
        form = HighlightThreadForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.created_by = request.user
            thread.save()
            messages.success(request, 'Thread added successfully!')
            return redirect(reverse('highlight_thread_list') + '?created=1')
    else:
        form = HighlightThreadForm()
    return render(request, 'community_engagement/hightlight_thread_create.html', {'form': form})

def HighlightThreadDetailView(request, pk):
    thread = get_object_or_404(HighlightThread, pk=pk)
    comments = thread.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.thread = thread
            comment.created_by = request.user
            comment.save()
            return redirect('highlight_thread_detail', pk=thread.pk)
    else:
        form = CommentForm()

    return render(request, 'community_engagement/hightlight_thread_detail.html', {'thread': thread, 'comments': comments, 'form': form})

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.thread = get_object_or_404(HighlightThread, pk=self.kwargs['pk'])
        form.save()
        return redirect('highlight_thread_detail', pk=self.kwargs['pk'])


# User Stories Views
def UserStoryListView(request):
    stories = UserStory.objects.all()
    return render(request, 'community_engagement/user_story_list.html', {'stories': stories})

# Create User Story
@login_required
def UserStoryCreateView(request):
    if request.method == 'POST':
        form = UserStoryForm(request.POST)
        if form.is_valid():
            user_story = form.save(commit=False)
            user_story.created_by = request.user
            user_story.save()
            messages.success(request, 'Story added successfully!')
            return redirect('user_story_list')
        else:
            messages.error(request, 'Error adding story. Please correct the form errors.')
    else:
        form = UserStoryForm()
    return render(request, 'community_engagement/user_story_create.html', {'form': form})

# Detail View of User Story
def UserStoryDetailView(request, pk):
    story = get_object_or_404(UserStory, pk=pk)
    comments = story.comments.all()

    if request.method == 'POST':
        form = StoryCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.story = story
            comment.created_by = request.user
            comment.save()
            return redirect('user_story_detail', pk=story.pk)
        else:
            messages.error(request, 'Error adding comment. Please correct the form errors.')
    else:
        form = StoryCommentForm()

    return render(request, 'community_engagement/user_story_detail.html', {'story': story, 'comments': comments, 'form': form})

# Edit User Story
@login_required
def UserStoryUpdateView(request, pk):
    story = get_object_or_404(UserStory, pk=pk)

    if request.method == 'POST':
        form = UserStoryForm(request.POST, instance=story)
        if form.is_valid():
            form.save()
            messages.success(request, 'Story updated successfully!')
            return redirect('user_story_list')
        else:
            messages.error(request, 'Error updating story. Please correct the form errors.')
    else:
        form = UserStoryForm(instance=story)

    return render(request, 'community_engagement/user_story_edit.html', {'form': form, 'story': story})

# Create Comment on User Story
@login_required
def StoryCommentCreateView(request, pk):
    story = get_object_or_404(UserStory, pk=pk)

    if request.method == 'POST':
        form = StoryCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.story = story
            comment.created_by = request.user
            comment.save()
            return redirect('user_story_detail', pk=story.pk)
        else:
            messages.error(request, 'Error adding comment. Please correct the form errors.')
    else:
        form = StoryCommentForm()

    return render(request, 'community_engagement/comment_form.html', {'form': form, 'story': story})

# Like User Story
@login_required
def like_story(request, pk):
    story = get_object_or_404(UserStory, pk=pk)
    story.likes.add(request.user)
    return redirect('user_story_detail', pk=story.pk)

# Dislike User Story
@login_required
def dislike_story(request, pk):
    story = get_object_or_404(UserStory, pk=pk)
    story.dislikes.add(request.user)
    return redirect('user_story_detail', pk=story.pk)