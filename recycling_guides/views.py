from django.shortcuts import render, get_object_or_404, redirect
from .models import RecyclingGuide
from .forms import RecyclingGuideForm

def recycling_guides_list(request):
    guides = RecyclingGuide.objects.all()
    return render(request, 'recycling_guides/list.html', {'guides': guides})

def recycling_guide_detail(request, pk):
    guide = get_object_or_404(RecyclingGuide, pk=pk)
    return render(request, 'recycling_guides/detail.html', {'guide': guide})

def add_recycling_guide(request):
    if request.method == 'POST':
        form = RecyclingGuideForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recycling_guides_list')
    else:
        form = RecyclingGuideForm()
    return render(request, 'recycling_guides/add.html', {'form': form})
from django.shortcuts import render

# Create your views here.
