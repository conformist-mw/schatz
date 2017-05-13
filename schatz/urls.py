from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^breed/$', views.breed),
    url(r'^puppies/$', views.puppies),
    url(r'^articles/$', views.articles),
    url(r'^contacts/$', views.contacts),
    url(r'^gallery/$', views.GalleryAlbums.as_view()),
    url(r'^gallery/tag/(?P<tag>.+)/$', views.TaggedList.as_view(), name='tagged'),
    url(r'^gallery/(?P<slug>.+)/$', views.PhotoGallery.as_view()),
]
