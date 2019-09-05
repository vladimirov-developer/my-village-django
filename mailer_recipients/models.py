from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Recipient(models.Model):

    content_type = models.ForeignKey(ContentType, verbose_name=_(u'content type'))
    email = models.EmailField(_(u'email'))

    class Meta:
        verbose_name = _(u'recipient')
        verbose_name_plural = _(u'recipients')

    def __unicode__(self):
        return self.email
