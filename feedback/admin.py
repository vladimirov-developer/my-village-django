# coding: utf-8
from django.contrib import admin
from mce_filebrowser.admin import MCEFilebrowserAdmin

from .models import Message


class MessageAdmin(MCEFilebrowserAdmin):

   list_display = ['full_name', 'email', 'phone', 'created_at']


admin.site.register(Message, MessageAdmin)
