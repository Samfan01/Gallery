from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    title = 'Photos covering the Stories Of my Travels'
    return render(request,'index.html',{'title':title,})
