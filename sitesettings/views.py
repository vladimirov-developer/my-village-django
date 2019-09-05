from django.http import HttpResponse, Http404
from .models import SiteSettings


def robots(request):
    obj = SiteSettings.objects.all()[0]
    return HttpResponse(obj.robots_txt, content_type='text/plain')


def sitemap(request):
    obj = SiteSettings.objects.all()[0]
    if not obj.sitemap_xml:
        raise Http404
    sitemap_file = open(obj.sitemap_xml.path, 'rb')
    return HttpResponse(content=sitemap_file.read(), content_type='application/xml')
