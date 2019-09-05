# coding: utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser
from plan.models import Stead


class User(AbstractUser):

    stead = models.ForeignKey(Stead, verbose_name=u'участок', null=True, blank=True)
