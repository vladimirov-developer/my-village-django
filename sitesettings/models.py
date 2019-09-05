# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse
from tinymce.models import HTMLField


class SiteSettings(models.Model):

    name = models.CharField(u'название сайта', max_length=255)
    main_title = models.CharField(u'заголовок на главной', max_length=255)
    main_preview = HTMLField(u'краткий текст на главной')
    main_text = HTMLField(u'текст на главной')
    phone1 = models.CharField(u'телефон 1', max_length=20, blank=True)
    phone2 = models.CharField(u'телефон 2', max_length=20, blank=True)
    email = models.EmailField(u'email', max_length=255, blank=True)
    address = models.CharField(u'адрес', max_length=255, blank=True)
    copyright = models.CharField(u'copyright', max_length=255, blank=True)

    plan_file1 = models.FileField(u'Утверждение проекта планировки территории КП',
        upload_to='sitesettings', null=True, blank=True)
    plan_file2 = models.FileField(u'Постановление о разработке проекта планировки территории КП',
        upload_to='sitesettings', null=True, blank=True)
    men_text = models.TextField(u'Текст мужчины на главной')
    robots_txt = models.TextField(u'robots.txt')
    sitemap_xml = models.FileField(u'sitemap.xml', upload_to='sitemap', null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'настройки сайта'
        verbose_name_plural = u'настройки сайта'


class BirdText(models.Model):
    sitesettings = models.ForeignKey(SiteSettings, related_name='bird_texts')
    text = models.TextField(u'текст')
    weight = models.PositiveIntegerField(u'вес', default=100)

    class Meta:
        verbose_name = u'фраза сороки'
        verbose_name_plural = u'фразы сороки'
        ordering = ['weight']
