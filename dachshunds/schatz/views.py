from django.shortcuts import render


def index(request):
    return render(request, 'schatz/index.html')


def gallery(request):
    return render(request, 'schatz/gallery.html')
