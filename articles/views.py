from django.views.generic import ListView, DetailView
from django.http import Http404

from .models import Article, DATA_TYPES


class ArticleMixin(object):

    model = Article

    def get_data_type(self):
        data_type = self.kwargs.get('data_type')
        if data_type not in map(lambda x: x[0], DATA_TYPES):
            raise Http404
        return data_type

    def get_queryset(self):
        data_type = self.get_data_type()
        qs = super(ArticleMixin, self).get_queryset()
        qs = qs.filter(is_active=True, data_type=data_type)
        return qs

    def get_context_data(self, **kwargs):
        data_type = self.get_data_type()
        kwargs.update({
            'data_type': data_type,
            'data_type_name': dict(DATA_TYPES)[data_type]
        })
        return super(ArticleMixin, self).get_context_data(**kwargs)


class ArticleListView(ArticleMixin, ListView):

    paginate_by = 9


class ArticleDetailView(ArticleMixin, DetailView):

    pass
