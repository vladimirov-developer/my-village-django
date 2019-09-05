# coding: utf-8
from django.contrib import admin
from mce_filebrowser.admin import MCEFilebrowserAdmin

from .models import Stead, Queue, Order, SteadDocFile


class QueueAdmin(MCEFilebrowserAdmin):

    pass


class SteadDocFileInline(admin.StackedInline):

    model = SteadDocFile

class SteadAdmin(MCEFilebrowserAdmin):

    inlines = [SteadDocFileInline]


class OrderAdmin(admin.ModelAdmin):

    list_display = ['full_name', 'email', 'phone', 'created_at']


admin.site.register(Queue, QueueAdmin)
admin.site.register(Stead, SteadAdmin)
admin.site.register(Order, OrderAdmin)
