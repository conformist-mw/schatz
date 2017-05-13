from os import path
from PIL import Image
from io import BytesIO
from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager
from django.core.files.base import ContentFile
from django.dispatch.dispatcher import receiver
from django.db.models.signals import pre_delete


class Album(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100)

    def get_cover(self):
        if Photo.objects.filter(album=self.id).filter(is_cover=True).count() > 0:
            return Photo.objects.filter(album=self.id).filter(is_cover=True).first()
        else:
            return None

    def __str__(self):
        return self.name


class Photo(models.Model):
    title = models.CharField(max_length=150)
    date_created = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='images/%Y/%m')
    thumbnail = models.ImageField(upload_to='thumbs/%Y/%m', editable=False)
    album = models.ForeignKey(Album)
    tags = TaggableManager()
    is_cover = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.is_cover:
            other_images = Photo.objects.filter(album=self.album).filter(is_cover=True)
            for photo in other_images:
                photo.is_cover = False
                photo.save()
        if not self.make_thumbnail():
            raise Exception('Чё то не получилось, давай ещё раз.')
        super(Photo, self).save(*args, **kwargs)

    def make_thumbnail(self):
        image = Image.open(self.photo)
        image.thumbnail(settings.THUMB_SIZE, Image.ANTIALIAS)
        fname, fext = path.splitext(self.photo.name)
        thumb_fname = '{}_thumb{}'.format(fname, fext)
        temp_file = BytesIO()
        image.save(temp_file, image.format)
        temp_file.seek(0)
        self.thumbnail.save(thumb_fname, ContentFile(temp_file.read()), save=False)
        temp_file.close()
        return True

    def __str__(self):
        return self.title


@receiver(pre_delete, sender=Photo)
def photo_delete_from_fs(sender, instance, **kwargs):
    instance.photo.delete(False)
    instance.thumbnail.delete(False)
