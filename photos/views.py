from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo,Category
# Create your views here.

def home(request):
    title = 'Photos covering the Stories Of my Travels'
    photo = Photo.photo_info()
    
    return render(request,'index.html',{'photos':photo})

def search_results(request):
    
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get('category')
        searched_photos = Category.search_by_category(search_term)
        photo = Photo.search_by_category(search_term)
        message = f'{search_term}'
        return render(request, 'search.html',{'message':message,'photos':photo})
    
    else:
        message = 'You have not searched any category!!'
        return render(request,'search.html',{'message':message})

def show_results(request):
    
    photo = Photo.show_by_location()
    
    return render(request,'location.html',{'photos':photo})
    