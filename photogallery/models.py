# coding: utf-8
from django.db import models
from tinymce.models import HTMLField
from django.core.urlresolvers import reverse


class Album(models.Model):

    title = models.CharField(u'заголовок', max_length=255)
    image = models.ImageField(u'обложка', upload_to='photogallery')
    content = HTMLField(u'содержимое', blank=True, null=True)
    is_active = models.BooleanField(u'активный', default=True)
    weight = models.PositiveIntegerField(default=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse(
            'photogallery_photo_list',
            args=[self.pk]
        )

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'фотоальбом'
        verbose_name_plural = u'фотоальбомы'
        ordering = ['weight', 'pk']


class Photo(models.Model):

    album = models.ForeignKey(Album, related_name='photos', verbose_name=u'альбом')
    title = models.CharField(u'заголовок', max_length=255, blank=True, null=True)
    image = models.ImageField(u'изображение', upload_to='photogallery')
    is_active = models.BooleanField(u'активный', default=True)
    weight = models.PositiveIntegerField(default=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title or self.image.path.split('/')[-1]

    class Meta:
        verbose_name = u'фотография'
        verbose_name_plural = u'фотографии'
        ordering = ['weight', 'pk']
