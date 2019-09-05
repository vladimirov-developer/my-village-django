from django.contrib import admin

from admin_messages.models import MessageSender, Message


class MessageSenderAdmin(admin.ModelAdmin):

    list_display = ['short_text', 'from_name', 'created_at']


class MessageAdmin(admin.ModelAdmin):

    list_display = ['user', 'short_text', 'created_at']


admin.site.register(MessageSender, MessageSenderAdmin)
admin.site.register(Message, MessageAdmin)
