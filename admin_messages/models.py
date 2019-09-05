# coding: utf-8
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import User



class MessageSender(models.Model):

    from_name = models.CharField(u'от кого', max_length=255, default=u'Администрация')
    text = models.TextField(u'текст сообщения')
    users = models.ManyToManyField(
        User, verbose_name=u'получатели', blank=True,
        help_text=u'Оставте поле пустым, если сообщение должно быть отправлено сразу всем пользователям.'
    )
    created_at = models.DateTimeField(u'дата создания', auto_now_add=True)

    @property
    def short_text(self):
        return self.text[:100] + '...'

    def __unicode__(self):
        return self.short_text

    class Meta:
        verbose_name = u'сообщение'
        verbose_name_plural = u'отправить сообщения'
        ordering = ['-created_at']


class Message(models.Model):
    user = models.ForeignKey(User, verbose_name=u'пользователь')
    from_name = models.CharField(u'от кого', max_length=255)
    text = models.TextField(u'сообщение')
    is_new = models.BooleanField(u'новое', default=True)
    created_at = models.DateTimeField(u'дата создания', auto_now_add=True)

    @property
    def short_text(self):
        return self.text[:100] + '...'

    def __unicode__(self):
        return self.user.username

    class Meta:
        verbose_name = u'сообщение'
        verbose_name_plural = u'отправленные сообщения'
        ordering = ['-created_at']


@receiver(post_save, sender=MessageSender)
def send_messages_on_save(sender, instance, **kwargs):
    from admin_messages.tasks import send_messages
    print '++++++++'
    print instance.pk
    send_messages.apply_async((instance.pk,), countdown=5)
