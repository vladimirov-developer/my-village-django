# coding: utf-8
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Message


class MessageListView(ListView):

    model = Message

    @method_decorator(login_required(login_url='/accounts/login/'))
    def dispatch(self, *args, **kwargs):
        return super(MessageListView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        qs = super(MessageListView, self).get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs

    def get_news_messages(self):
        qs = self.get_queryset()
        return qs.filter(is_new=True)

    def mark_as_read(self):
        qs = self.get_news_messages()
        qs.update(is_new=False)

    def get_context_data(self, **kwargs):
        self.new_list = list(self.get_news_messages().values_list('pk', flat=True))
        self.mark_as_read()
        kwargs.update({
            'new_list': self.new_list
        })
        return super(MessageListView, self).get_context_data(**kwargs)
