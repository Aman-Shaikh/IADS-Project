from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import HighlightThread, Comment
from .ce_forms import HighlightThreadForm, CommentForm

class HighlightThreadListView(ListView):
    model = HighlightThread
    template_name = 'community_engagement/highlight_thread_list.html'
    context_object_name = 'threads'

class HighlightThreadDetailView(DetailView):
    model = HighlightThread
    template_name = 'community_engagement/highlight_thread_detail.html'
    context_object_name = 'thread'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(thread=self.object)
        context['form'] = CommentForm()
        return context

class HighlightThreadCreateView(LoginRequiredMixin, CreateView):
    model = HighlightThread
    form_class = HighlightThreadForm
    template_name = 'community_engagement/highlight_thread_create.html'
    success_url = '/forum-highlights/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.thread = get_object_or_404(HighlightThread, pk=self.kwargs['pk'])
        form.save()
        return redirect('highlight_thread_detail', pk=self.kwargs['pk'])
