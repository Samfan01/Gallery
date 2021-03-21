from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo
# Create your views here.

def home(request):
    title = 'Photos covering the Stories Of my Travels'
    photo = Photo.photo_info()
    
    return render(request,'index.html',{'photos':photo})
