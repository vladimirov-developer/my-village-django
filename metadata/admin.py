from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ungettext

from .models import Metadata
from .widgets import AdminSmallTextareaWidget

from django.contrib import admin


class MetadataAdminMixin(object):

    change_form_template = 'metadata/admin/change_form.html'


class MetadataModelAdmin(MetadataAdminMixin, admin.ModelAdmin):
    pass


class MetadataAdmin(admin.ModelAdmin):

    list_display = (
        'url_path', 'title', 'changefreq', 'lastmod', 'language', 'enabled',
    )
    list_display_links = ('url_path', 'title')
    list_filter = ('enabled', 'lastmod')
    formfield_overrides = {
        models.TextField: {'widget': AdminSmallTextareaWidget},
    }


admin.site.register(Metadata, MetadataAdmin)
