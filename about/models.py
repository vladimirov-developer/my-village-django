# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse
from tinymce.models import HTMLField


class About(models.Model):

    title = models.CharField(u'заголовок', max_length=255)
    content = HTMLField(u'содержимое')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'о поселке'
        verbose_name_plural = u'о поселке'
