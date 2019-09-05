from django.template import Library

from django.contrib.auth.forms import AuthenticationForm


register = Library()


@register.inclusion_tag('accounts/login_form.html')
def login_form():
    return {'form': AuthenticationForm()}


@register.filter('startswith')
def startswith(text, starts):
    return text.startswith(starts)
