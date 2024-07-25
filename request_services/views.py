from django.shortcuts import render, redirect
from .forms import ServiceRequestForm
from django.contrib import messages

def request_service_view(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your service request has been submitted!')
            return redirect('home')
    else:
        form = ServiceRequestForm()
    return render(request, 'request_services/request_service.html', {'form': form})

