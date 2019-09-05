# coding: utf-8
from accounts.models import User
from celery.task import task
from mailer import Mailer

from .models import MessageSender, Message


@task(name='Message sender')
def send_messages(obj_id, **kwargs):
    obj = MessageSender.objects.get(pk=obj_id)
    users_qs = obj.users.all()
    if not users_qs:
        users_qs = User.objects.all()
    for user in users_qs:
        message = Message.objects.create(
            user=user,
            from_name=obj.from_name,
            text=obj.text
        )
        if user.email:
            try:
                Mailer.send(
                    recipients=[user.email],
                    template_name='admin_messages/mail',
                    context_data={'message': message}
                )
            except:
                pass
