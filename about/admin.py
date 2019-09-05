# coding: utf-8
from django.contrib import admin
from mce_filebrowser.admin import MCEFilebrowserAdmin

from .models import About


class AboutAdmin(MCEFilebrowserAdmin):

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(About, AboutAdmin)
