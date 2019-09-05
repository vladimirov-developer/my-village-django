# coding: utf-8
from django.contrib import admin
from mce_filebrowser.admin import MCEFilebrowserAdmin

from .models import SiteSettings, BirdText


class BirdTextInline(admin.StackedInline):
    model = BirdText


class SiteSettingsAdmin(MCEFilebrowserAdmin):

    inlines = [BirdTextInline]

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(SiteSettings, SiteSettingsAdmin)
