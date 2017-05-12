from django.shortcuts import render
from django.views.generic import ListView
from .models import Album, Photo


class GalleryAlbums(ListView):
    model = Album
    context_object_name = 'albums'


class PhotoGallery(ListView):
    model = Photo
    context_object_name = 'photos'

    def get_queryset(self, *args, **kwargs):
        album_id = Album.objects.filter(slug=self.kwargs['slug'])
        return Photo.objects.filter(album_id=album_id)


class TaggedList(ListView):
    model = Photo
    context_object_name = 'photos'

    def get_queryset(self, *args, **kwargs):
        return Photo.objects.filter(tags__slug=self.kwargs['tag'])


def index(request):
    return render(request, 'schatz/index.html')


def gallery(request):
    return render(request, 'schatz/gallery.html')
