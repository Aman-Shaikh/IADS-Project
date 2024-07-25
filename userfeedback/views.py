from django.shortcuts import render, redirect
from .forms import ComplaintForm
from django.contrib import messages

def user_complaint_view(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your complaint!')
            return redirect('home')
    else:
        form = ComplaintForm()
    return render(request, 'userfeedback/user_complaint.html', {'form': form})
