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
class UserStoryListView(ListView):
    model = UserStory
    template_name = 'community_engagement/user_story_list.html'
    context_object_name = 'stories'

class UserStoryCreateView(LoginRequiredMixin, CreateView):
    model = UserStory
    form_class = UserStoryForm
    template_name = 'community_engagement/user_story_create.html'
    success_url = reverse_lazy('user_story_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class UserStoryDetailView(DetailView):
    model = UserStory
    template_name = 'community_engagement/user_story_detail.html'
    context_object_name = 'story'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = StoryCommentForm()
        return context

class UserStoryUpdateView(LoginRequiredMixin, UpdateView):
    model = UserStory
    form_class = UserStoryForm
    template_name = 'community_engagement/user_story_edit.html'
    success_url = reverse_lazy('user_story_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class StoryCommentCreateView(LoginRequiredMixin, CreateView):
    model = StoryComment
    form_class = StoryCommentForm
    template_name = 'community_engagement/comment_form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.story = get_object_or_404(UserStory, pk=self.kwargs['pk'])
        form.save()
        return redirect('user_story_detail', pk=self.kwargs['pk'])

