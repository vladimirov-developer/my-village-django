# coding: utf-8
from django.contrib import admin
from mce_filebrowser.admin import MCEFilebrowserAdmin

from .models import Album, Photo


class PhotoInline(admin.StackedInline):

    model = Photo


class AlbumAdmin(MCEFilebrowserAdmin):

    list_display = ['title', 'weight', 'is_active']
    list_editable = ['weight', 'is_active']
    inlines = [PhotoInline]


admin.site.register(Album, AlbumAdmin)
