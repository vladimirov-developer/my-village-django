# coding: utf-8
from django.db import models
from tinymce.models import HTMLField


QUEUE = (
    (1, u'первая'),
    (2, u'вторая')
)


class Queue(models.Model):

    queue = models.PositiveIntegerField(u'номер очереди', choices=QUEUE, unique=True)
    title = models.CharField(u'заголовок', max_length=255)
    preview = HTMLField(u'краткое содержимое', blank=True)
    content = HTMLField(u'содержимое', blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'очередь строительства'
        verbose_name_plural = u'очереди строительства'


STATUS = (
    (0, u'свободен'),
    (1, u'забронирован'),
    (2, u'продан'),
)


class Stead(models.Model):

    queue = models.ForeignKey(Queue, verbose_name='очередь')
    status = models.PositiveIntegerField(default=0, choices=STATUS)
    number = models.PositiveIntegerField(u'номер участка', null=True)
    title = models.CharField(u'заголовок', max_length=255)
    image = models.ImageField(u'изображение', upload_to='plan', null=True, blank=True)
    area = models.CharField(u'площадь участка', max_length=255, blank=True)
    price = models.CharField(u'цена', max_length=255, blank=True)
    content = HTMLField(u'содержимое', blank=True)
    id_stead = models.CharField(max_length=10, unique=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'участок'
        verbose_name_plural = u'участки'


class Order(models.Model):

    stead = models.ForeignKey(Stead, verbose_name=u'участок')
    full_name = models.CharField(u'ФИО', max_length=255)
    phone = models.CharField(u'телефон', max_length=50, blank=True)
    email = models.EmailField(u'email', max_length=255, blank=True)
    text = models.TextField(u'текст сообщения', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.full_name

    class Meta:
        verbose_name = u'заявка бронирования участка'
        verbose_name_plural = u'заявки бронирования участков'
        ordering = ['-created_at']


class SteadDocFile(models.Model):

    stead = models.ForeignKey(Stead, verbose_name=u'участок', related_name='user_files')
    name = models.CharField(u'название документа', max_length=255)
    file = models.FileField(u'документ', upload_to='plan')
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'документ'
        verbose_name_plural = u'документы собственика'
