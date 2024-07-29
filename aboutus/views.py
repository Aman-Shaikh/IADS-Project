from django.shortcuts import render, get_object_or_404
from .models import TeamMember, Section
from .forms import TeamMemberForm, SectionForm
from django.contrib.auth.decorators import login_required


def team_member_list(request):
    members = TeamMember.objects.all()
    return render(request, 'aboutus/team_member_list.html', {'members': members})


def team_member_detail(request, pk):
    member = get_object_or_404(TeamMember, pk=pk)
    return render(request, 'aboutus/team_member_detail.html', {'member': member})


def section_list(request):
    sections = Section.objects.all()
    return render(request, 'aboutus/section_list.html', {'sections': sections})


def section_detail(request, pk):
    section = get_object_or_404(Section, pk=pk)
    return render(request, 'aboutus/section_detail.html', {'section': section})
