from django.conf.urls import url
from django.views.generic import TemplateView

from admin_messages.views import MessageListView
from .views import login, logout, profile, user_stead_info, user_stead_docs


urlpatterns = [
    url(r'^login/$', login, name='accounts_login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='accounts_logout'),
    url(r'^profile/$', profile, name="profile_page"),
    url(r'^profile/messages/$', MessageListView.as_view(), name="profile_messages"),
    url(r'^profile/stead-info/$', user_stead_info, name="profile_stead"),
    url(r'^profile/docs/$', user_stead_docs, name="profile_docs"),
]
