from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect

# Create your views here.
def landing(request):
    pics = Image.all_pics()
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