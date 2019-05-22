from django.shortcuts import render,redirect
from .models import Image,Location,Category
# Create your views here.

def welcome(request):
    photo_gallery=Image.all_images()
    return render(request,'gallery/welcome.html',{'photo_gallery':photo_gallery})

def search_results(request):

    if 'image'  in request.GET and request.GET['image']:
        search_term = request.GET.get('image')
        searched_images=Image.search_by_title(search_term)
        message =f"{search_term}"

        return render(request,'gallery/search.html',{'message':message,'searched_images':searched_images})

    else:
        message = "You havent searched for any term"
        return render(request,'gallery/search.html',{'message':message})
