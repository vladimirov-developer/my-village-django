# coding: utf-8
from django.views.generic import ListView
from django.shortcuts import get_object_or_404

from .models import Album, Photo


class AlbumListView(ListView):

    model = Album
    template_name = 'photogallery/album_list.html'
    paginate_by = 12

    def get_queryset(self):
        qs = super(AlbumListView, self).get_queryset()
        qs = qs.filter(is_active=True)
        return qs


class PhotoListView(ListView):

    model = Photo
    template_name = 'photogallery/photo_list.html'
    paginate_by = 12

    def get_album(self):
        qs = Album.objects.filter(is_active=True)
        obj = get_object_or_404(qs, pk=self.kwargs.get('album_id'))
        return obj

    def get_queryset(self):
        qs = super(PhotoListView, self).get_queryset()
        album = self.get_album()
        qs = qs.filter(is_active=True)
        qs = qs.filter(album=album)
        return qs

    def get_context_data(self, **kwargs):
        kwargs.update({'album': self.get_album()})
        return super(PhotoListView, self).get_context_data(**kwargs)
