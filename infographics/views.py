# infographics/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Infographic
from .forms import InfographicForm

def infographic_list(request):
    infographics = Infographic.objects.all()
    return render(request, 'infographics/infographic_list.html', {'infographics': infographics})

def infographic_detail(request, pk):
    infographic = get_object_or_404(Infographic, pk=pk)
    return render(request, 'infographics/infographic_detail.html', {'infographic': infographic})

def infographic_new(request):
    if request.method == "POST":
        form = InfographicForm(request.POST, request.FILES)
        if form.is_valid():
            infographic = form.save()
            return redirect('infographic_detail', pk=infographic.pk)
    else:
        form = InfographicForm()
    return render(request, 'infographics/infographic_edit.html', {'form': form})

def infographic_edit(request, pk):
    infographic = get_object_or_404(Infographic, pk=pk)
    if request.method == "POST":
        form = InfographicForm(request.POST, request.FILES, instance=infographic)
        if form.is_valid():
            infographic = form.save()
            return redirect('infographic_detail', pk=infographic.pk)
    else:
        form = InfographicForm(instance=infographic)
    return render(request, 'infographics/infographic_edit.html', {'form': form})
