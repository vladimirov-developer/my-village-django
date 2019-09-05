from django.http import Http404
from django.shortcuts import render
from about.models import About


def about_vilage(request):
    try:
        obj = About.objects.all()[0]
    except IndexError:
        raise Http404
    return render(request, 'pages/village.html', context={'object': obj})
