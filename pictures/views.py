from django.shortcuts import render

# Create your views here.
def landing(request):
    pics = Image.all_pics()
    return render(request,'index.html',{"pics": pics})