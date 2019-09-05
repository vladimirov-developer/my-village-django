# coding: utf-8
from django.contrib import admin
from mce_filebrowser.admin import MCEFilebrowserAdmin

from .models import Article


class ArticleAdmin(MCEFilebrowserAdmin):

    list_display = ['title', 'data_type', 'created_at', 'is_active']
    list_editable = ['is_active']
    list_filter = ['data_type']


admin.site.register(Article, ArticleAdmin)
