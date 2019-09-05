# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse
from tinymce.models import HTMLField


DATA_TYPES = (
    ('news', u'Новости'),
    ('articles', u'Статьи')
)


class Article(models.Model):

    data_type = models.CharField(
        u'тип публикации',
        choices=DATA_TYPES,
        max_length=10
    )
    title = models.CharField(u'заголовок', max_length=255)
    image = models.ImageField(u'зображение', upload_to='articles')
    preview = HTMLField(u'анонс')
    content = HTMLField(u'содержимое')
    is_active = models.BooleanField(u'активный', default=True)
    created_at = models.DateTimeField(u'дата публикации', auto_now_add=True)

    def get_absolute_url(self):
        return reverse(
            'articles_article_detail',
            args=[self.data_type, self.pk]
        )

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'публикация'
        verbose_name_plural = u'публикации'
        ordering = ['-created_at']
