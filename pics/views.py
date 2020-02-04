from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Image
# Create your views here.

def landing(request):
    pics = Image.objects.all()
    return render(request,'index.html',{"pics": pics})

def search(request):
    if 'image' in request.GET and request.GET['image']:
        search_input = request.GET.get('image')
        searched_images = Image.search_by_category(search_input)
        message = f"{search_input}"

        return render(request, 'search.html', {"message":message, "images":searched_images})

    else:
        message = "Please input something in the search field"
    return render(request, 'search.html', {'message':message})


def places(request):
  
    
    return render(request,'locs.html')


def somewhere(request):
    catt = 'somewhere' 
    pics = Image.objects.filter(location__locname=catt).all()
    
    return render(request,'somewhere.html',{"pics":pics})
    
def wild(request):
    catt = 'wild' 
    pics = Image.objects.filter(location__locname=catt).all()
    
    return render(request,'wild.html',{"pics":pics})
def france(request):
    catt = 'france' 
    pics = Image.objects.filter(location__locname=catt).all()
    
    return render(request,'france.html',{"pics":pics})
def mombasa(request):
    catt = 'mombasa' 
    pics = Image.objects.filter(location__locname=catt).all()
    
    return render(request,'mombasa.html',{"pics":pics})
def nairobi(request):
    catt = 'nairobi' 
    pics = Image.objects.filter(location__locname=catt).all()
    
    return render(request,'nairobi.html',{"pics":pics})
def belgium(request):
    catt = 'belgium' 
    pics = Image.objects.filter(location__locname=catt).all() 
    
    return render(request,'belgium.html',{"pics":pics})