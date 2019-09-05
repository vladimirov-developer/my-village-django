from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login as login_function
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import login as login_view
from django.contrib.auth.views import logout as logout_view
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required

from sessionprofile.models import SessionProfile


def login(request, *args, **kwargs):
    if request.is_ajax():
        template_name = 'accounts/login_form.html'
    else:
        template_name = 'accounts/login_page.html'
    form = AuthenticationForm(data=request.POST)
    response = login_view(
        request, template_name=template_name,  *args, **kwargs
    )
    response.delete_cookie('phpbb3_k23kc_u')
    response.delete_cookie('phpbb3_k23kc_k')
    response.delete_cookie('phpbb3_k23kc_sid')
    if request.method == 'POST':
        if 'remember' not in request.POST:
            request.session.set_expiry(0)
        else:
            request.session.set_expiry(None)
    if form.is_valid():
        return HttpResponse('Success auth')
    return response


def logout(request, *args, **kwargs):
    if request.user.is_authenticated():
        SessionProfile.objects.filter(user_id=request.user.pk).delete()
    response = logout_view(request, *args, **kwargs)
    response.delete_cookie('phpbb3_k23kc_u')
    response.delete_cookie('phpbb3_k23kc_k')
    response.delete_cookie('phpbb3_k23kc_sid')
    return response


@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request, 'accounts/profile.html')


@login_required(login_url='/accounts/login/')
def user_stead_info(request):
    if not request.user.stead:
        raise Http404
    return render(request, 'accounts/stead.html', context={'object': request.user.stead})


@login_required(login_url='/accounts/login/')
def user_stead_docs(request):
    if not request.user.stead:
        raise Http404
    return render(request, 'accounts/documents.html', context={'object': request.user.stead})
