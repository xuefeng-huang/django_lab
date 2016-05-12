from django.shortcuts import render
from django.http import Http404
from .models import Album


# Create your views here.
def index(req):
    all_albums = Album.objects.all()
    context = {'albums' : all_albums}
    return render(req, 'index.html', context)
    
def detail(req, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404('album does not exist')
    return render(req, 'detail.html', {'album' : album})


