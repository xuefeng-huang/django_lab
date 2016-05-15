from django.shortcuts import render, get_object_or_404
from .models import Album, Song


# Create your views here.
def index(req):
    all_albums = Album.objects.all()
    context = {'albums' : all_albums}
    return render(req, 'index.html', context)
    
def detail(req, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(req, 'detail.html', {'album' : album})
    
def favorite(req, album_id):
    album = get_object_or_404(Album, pk=album_id)
    
    try:
        selected_song = album.song_set.get(pk=req.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(req, 'detail.html', {
            'album': album,
            'error_message': 'did not select a valid song',
        })
        
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(req, 'detail.html', {'album' : album})
        
        



