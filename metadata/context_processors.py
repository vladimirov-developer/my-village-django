from django.utils.functional import SimpleLazyObject
from django.utils.safestring import mark_safe
from django.utils.translation import get_language
from django.db.models import Q
from django.contrib.sites.models import Site

from .models import Metadata
from .settings import CONFIG


class MetadataContextObject(object):

    def __init__(self, full_path, path, site):
        metadata = self._get_metadata(full_path, path, site)
        if metadata and metadata.enabled:
            self.title = self._get_title(metadata, site)
            self.keywords = metadata.keywords
            self.description = metadata.description
            self.enabled = True
        else:
            self.title = self.keywords = self.description = ''
            self.enabled = False

    def _get_metadata(self, full_path, path, site):
        queryset = Metadata.objects.filter(
            Q(url_path=full_path) | Q(url_path=path),
            language=get_language(),
            sites=site,
            enabled=True,
        ).order_by('-url_path')

        try:
            return queryset[0]
        except IndexError:
            return None

    def _get_title(self, metadata, site):
        if not metadata.title:
            return ''
        titles = [metadata.title]
        if metadata.title_extend:
            titles.append(site.name)
        if CONFIG['TITLE_REVERSED']:
            titles.reverse()
        return mark_safe(CONFIG['TITLE_SEPARATOR'].join(titles))


def metadata(request):
    full_path = request.get_full_path()
    path = request.path
    site = Site.objects.all()[0]

    return {
        'metadata': SimpleLazyObject(
            lambda: MetadataContextObject(full_path, path, site)
        )
    }