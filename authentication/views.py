from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

from authentication.forms import CustomAuthenticationForm,CustomUserCreationForm


def home(request):
    return render(request, 'home.html')

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Signup successful! Welcome, {}'.format(user.username))
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'authentication/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful! Welcome back, {}'.format(user.username))
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'authentication/login.html', {'form': form})
def logout_view(request):
    logout(request)
    return redirect('home')
