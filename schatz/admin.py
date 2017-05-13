from django.contrib import admin
from .models import Album, Photo


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 2


class PhotoAdmin(admin.ModelAdmin):
    pass


class AlbumAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)
