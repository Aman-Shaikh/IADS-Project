from django.shortcuts import render, get_object_or_404, redirect
from .models import TeamMember, Section
from .forms import TeamMemberForm, SectionForm
from django.contrib.auth.decorators import login_required

@login_required
def team_member_list(request):
    members = TeamMember.objects.all()
    return render(request, 'aboutus/team_member_list.html', {'members': members})

@login_required
def team_member_detail(request, pk):
    member = get_object_or_404(TeamMember, pk=pk)
    return render(request, 'aboutus/team_member_detail.html', {'member': member})

def section_list(request):
    sections = Section.objects.all()
    return render(request, 'aboutus/section_list.html', {'sections': sections})

def section_detail(request, pk):
    section = get_object_or_404(Section, pk=pk)
    return render(request, 'aboutus/section_detail.html', {'section': section})

@login_required
def add_section(request):
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('section_list')
    else:
        form = SectionForm()
    return render(request, 'aboutus/add_section.html', {'form': form})

@login_required
def section_detail(request, pk):
    section = get_object_or_404(Section, pk=pk)
    return render(request, 'aboutus/section_detail.html', {'section': section})

@login_required
def add_team_member(request):
    if request.method == 'POST':
        form = TeamMemberForm(request.POST, request.FILES)  # Handle file uploads
        if form.is_valid():
            form.save()
            return redirect('team_member_list')
    else:
        form = TeamMemberForm()
    return render(request, 'aboutus/add_team_member.html', {'form': form})

@login_required
def edit_team_member(request, pk):
    member = get_object_or_404(TeamMember, pk=pk)
    if request.method == 'POST':
        form = TeamMemberForm(request.POST, request.FILES, instance=member)  # Handle file uploads
        if form.is_valid():
            form.save()
            return redirect('team_member_detail', pk=pk)
    else:
        form = TeamMemberForm(instance=member)
    return render(request, 'aboutus/edit_team_member.html', {'form': form, 'member': member})
