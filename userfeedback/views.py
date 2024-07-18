from django.shortcuts import render, redirect
from .forms import FeedbackForm
from django.contrib import messages

def user_feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            # For now, we'll just print it to the console (you might save it to a database)
            print(form.cleaned_data)
            messages.success(request, 'Thank you for your feedback!')
            return redirect('home')
    else:
        form = FeedbackForm()
    return render(request, 'userfeedback/user_complaint.html', {'form': form})