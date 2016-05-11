from django.shortcuts import render


# Create your views here.
def index(req):
    return render(req, 'index.html', {})
    
def detail(req, album_id):
    return render(req, 'detail.html', {'album_id' : album_id})


