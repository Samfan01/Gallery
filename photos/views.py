from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo,Category,Location
# Create your views here.

def home(request):
    title = 'Photos covering the Stories Of my Travels'
    photo = Photo.photo_info()
    locations = Location.by_location()
    
    return render(request,'index.html',{'photos':photo,'locations':locations})

def search_results(request):
    
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get('category')
        searched_photos = Photo.search_by_category(search_term)
        message = f'{search_term}'
        return render(request, 'search.html',{'message':message,'photos':searched_photos})
    
    else:
        message = 'You have not searched any category!!'
        return render(request,'search.html',{'message':message})

def show_results(request):
    
    photo = Photo.show_by_location()
    
    return render(request,'location.html',{'photos':photo})
    