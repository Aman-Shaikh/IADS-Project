# userfeedback/views.py

from django.shortcuts import render

def user_feedback(request):
    # Your view logic here
    return render(request, 'userfeedback/user_feedback.html')  # Example template rendering
