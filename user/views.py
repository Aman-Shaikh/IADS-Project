from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserLoginForm, ProfileEditForm, ForgotPasswordForm
from .models import UserProfile, UserHistory, UserSession
from django.http import HttpResponse


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserRegistrationForm()
    return render(request, 'main/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = UserLoginForm()
    return render(request, 'main/login.html', {'form': form})


@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile_edit')
    else:
        form = ProfileEditForm(instance=request.user.userprofile)
    return render(request, 'user/profile_edit.html', {'form': form})


def forgot_password(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            # Implement password reset logic here
            pass
    else:
        form = ForgotPasswordForm()
    return render(request, 'user/forgot_password.html', {'form': form})


@login_required
def user_history(request):
    history = UserHistory.objects.filter(user=request.user)
    return render(request, 'user/user_history.html', {'history': history})


def user_history_view(request):
    if request.user.is_authenticated:
        sessions = UserSession.objects.filter(user=request.user)
        response = '<h2>User History</h2><ul>'
        for session in sessions:
            response += f'<li>{session.created_at}: {session.session_data}</li>'
        response += '</ul>'
        return HttpResponse(response)
    else:
        return redirect('login')
