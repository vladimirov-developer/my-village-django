from django.template import Library

from feedback.forms import MessageForm


register = Library()


@register.inclusion_tag('feedback/feedback_form.html')
def feedback_form():
    return {'form': MessageForm()}
