"""tokarevo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from about.views import about_vilage
from sitesettings.views import robots, sitemap


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="main_page"),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^mce_filebrowser/', include('mce_filebrowser.urls')),

    url(r'^photos/', include('photogallery.urls')),
    url(r'^publications/', include('articles.urls')),
    url(r'^village/', about_vilage, name="village_page"),
    url(r'^feedback/', include('feedback.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^contacts/', TemplateView.as_view(template_name='contacts/contacts.html'), name="contacts_page"),
    url(r'^login_page/', TemplateView.as_view(template_name='accounts/login_page.html'), name="login_page"),
    url(r'^404/', TemplateView.as_view(template_name='404.html'), name="not_found"),
    url(r'^msg/', TemplateView.as_view(template_name='accounts/msg.html'), name="not_found"),
    url(r'^reservation/', TemplateView.as_view(template_name='plan/reservation.html'), name="reservation_page"),
    url(r'^general/', include('plan.urls')),
    url(r'^robots\.txt', robots, name="robots"),
    url(r'^sitemap\.xml', sitemap, name="sitemap"),
]
