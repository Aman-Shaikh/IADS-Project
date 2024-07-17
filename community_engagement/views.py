from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import HighlightThread, Comment
from .forms import HighlightThreadForm, CommentForm

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
            return redirect('highlight_thread_list')
    else:
        form = HighlightThreadForm()
    return render(request, 'community_engagement/highlight_thread_create.html', {'form': form})

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

    return render(request, 'community_engagement/highlight_thread_detail.html', {'thread': thread, 'comments': comments, 'form': form})

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.thread = get_object_or_404(HighlightThread, pk=self.kwargs['pk'])
        form.save()
        return redirect('highlight_thread_detail', pk=self.kwargs['pk'])
