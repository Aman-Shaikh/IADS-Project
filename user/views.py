# user/views.py

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import ProfileEditForm, ForgotPasswordForm

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile_edit')
    else:
        form = ProfileEditForm(instance=request.user)
    return render(request, 'user/profile_edit.html', {'form': form})

class ForgotPasswordView(PasswordResetView):
    template_name = 'user/forgot_password.html'
    form_class = ForgotPasswordForm

@login_required
def user_history(request):
    # Implement user history retrieval logic here
    return render(request, 'user/user_history.html')

def logout(request):
    # Implement user history retrieval logic here
    return render(request, 'user/logged_out.html')