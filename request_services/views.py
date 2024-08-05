from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ServiceRequestForm
from .models import ServiceRequest

@login_required
def request_service_view(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user  # Associate the current user
            service_request.save()
            messages.success(request, 'Your service request has been submitted!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ServiceRequestForm()
    return render(request, 'request_services/request_service.html', {'form': form})

@login_required
def service_requests_view(request):
    # Fetch the service requests made by the current user
    service_requests = ServiceRequest.objects.filter(user=request.user)  # Filter by user, not email
    return render(request, 'request_services/service_requests_view.html', {'service_requests': service_requests})
