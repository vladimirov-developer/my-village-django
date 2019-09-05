# coding: utf-8
from django.db import models


class Message(models.Model):

    full_name = models.CharField(u'имя', max_length=255)
    phone = models.CharField(u'телефон', max_length=20, blank=True)
    email = models.EmailField(u'email', max_length=255, blank=True)
    text = models.TextField(u'текст сообщения')
    created_at = models.DateTimeField(u'дата создания', auto_now_add=True)

    def __unicode__(self):
        return self.full_name

    class Meta:
        verbose_name = u'сообщение обратной связи'
        verbose_name_plural = u'сообщения обратной связи'
        ordering = ['-created_at']
