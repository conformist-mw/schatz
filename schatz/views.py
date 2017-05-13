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

    def get_context_data(self, **kwargs):
        context = super(PhotoGallery, self).get_context_data(**kwargs)
        tags_set = [tag for photo in context['object_list'] for tag in photo.tags.all()]
        context['tags_set'] = set(tags_set)
        context['test'] = 'pizdec'
        return context


class TaggedList(ListView):
    model = Photo
    context_object_name = 'photos'

    def get_queryset(self, *args, **kwargs):
        return Photo.objects.filter(tags__slug=self.kwargs['tag'])

    def get_context_data(self, **kwargs):
        context = super(TaggedList, self).get_context_data(**kwargs)
        tags_set = [tag for photo in context['object_list'] for tag in photo.tags.all()]
        context['tags_set'] = set(tags_set)
        context['test'] = 'pizdec'
        return context


def index(request):
    return render(request, 'schatz/index.html')


def breed(request):
    return render(request, 'schatz/breed.html')


def puppies(request):
    return render(request, 'schatz/puppies.html')


def articles(request):
    return render(request, 'schatz/articles.html')


def contacts(request):
    return render(request, 'schatz/contacts.html')
