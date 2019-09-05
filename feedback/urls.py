from django.conf.urls import url
from .views import feedback_view


urlpatterns = [
    url(r'^form/$', feedback_view, name="feedback_feedback_form"),
]
