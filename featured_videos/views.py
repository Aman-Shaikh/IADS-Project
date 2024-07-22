from django.shortcuts import render, redirect,reverse
from .models import FeaturedVideo
from .forms import FeaturedVideoForm

def featured_videos_list(request):
    videos = FeaturedVideo.objects.all()
    return render(request, 'featured_videos/featured_videos_list.html', {'videos': videos})

def add_featured_video(request):
    if request.method == 'POST':
        form = FeaturedVideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('featured_videos_list'))
    else:
        form = FeaturedVideoForm()
    return render(request, 'featured_videos/add_featured_video.html', {'form': form})
