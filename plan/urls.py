from django.conf.urls import url
from .views import general, plan, stead, stead_edit, stead_reservation, order_view


urlpatterns = [
    url(r'^plan/$', general, name="plan_general"),
    url(r'^plan/(?P<queue>\d+)/$', plan, name='plan_queue'),
    url(r'^plan/(?P<queue>\d+)/(?P<stead_id>\w+)/$', stead, name='plan_stead_detail'),
    url(r'^plan/(?P<queue>\d+)/edit/(?P<stead_id>\w+)/$', stead_edit, name='plan_stead_edit'),

    url(r'^booking/(?P<pk>\d+)/$', stead_reservation, name='plan_stead_reservation'),
    url(r'^booking/(?P<pk>\d+)/form/$', order_view, name='plan_stead_reservation_form'),
]
