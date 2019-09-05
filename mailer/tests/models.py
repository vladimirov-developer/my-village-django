from django.db import models


class Message(models.Model):

    full_name = models.CharField(max_length=100)
    text = models.TextField()

    class Meta:
        app_label = 'mailer'
        verbose_name = u'feedback message'


class Recipient(models.Model):

    email = models.EmailField()

    class Meta:
        ordering = ['email']
        app_label = 'mailer'
