from django.shortcuts import render

from mailer_recipients.base import RecipientsMailer

from .forms import MessageForm


def feedback_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save()
            RecipientsMailer.send(
                request=request,
                object=message,
                template_name='feedback/mail',
            )
            return render(request, 'feedback/feedback_form.html', {
                'form': MessageForm(),
                'success': True
            })
    else:
        form = MessageForm()
    return render(request, 'feedback/feedback_form.html', {
        'form': form,
        'success': False
    })
