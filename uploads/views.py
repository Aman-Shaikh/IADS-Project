from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UploadedFile


def upload_file_view(request):
    if request.method == 'POST':
        file = request.FILES['file']
        description = request.POST['description']
        uploaded_file = UploadedFile(file=file, description=description)
        uploaded_file.save()
        return HttpResponse('File uploaded successfully')
    return HttpResponse('Upload file form will be here')
