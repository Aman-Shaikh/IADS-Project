from django.shortcuts import render

def getting_started(request):
    return render(request, 'getting_started/getting_started.html')
