from sitesettings.models import SiteSettings


def sitesettings(request):
    try:
        obj = SiteSettings.objects.all()[0]
    except IndexError:
        obj = None
    return {
        'sitesettings': obj
    }
