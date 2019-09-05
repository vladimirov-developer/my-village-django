from admin_messages.models import Message


def new_message_count(request):
    new_messages = 0
    if request.user.is_authenticated():
        new_messages = Message.objects.filter(user=request.user, is_new=True).count()
    return {
        'new_messages': new_messages
    }
