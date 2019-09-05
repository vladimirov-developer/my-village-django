from django.conf.urls import url
from django.views.generic import TemplateView

from .views import ArticleListView, ArticleDetailView


urlpatterns = [
    url(r'^(?P<data_type>\w+)/$',
        ArticleListView.as_view(),
        name='articles_article_list'),
    url(r'^(?P<data_type>\w+)/(?P<pk>\d+)/$',
        ArticleDetailView.as_view(),
        name='articles_article_detail'),
]
