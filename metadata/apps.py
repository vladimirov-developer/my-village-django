from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class MetadataConfig(AppConfig):

    name = 'metadata'
    verbose_name = _('Page Metadata')
