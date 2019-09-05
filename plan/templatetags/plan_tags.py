from django.template import Library

from plan.forms import OrderForm


register = Library()


@register.inclusion_tag('plan/order_form.html')
def order_form(stead):
    return {'form': OrderForm(), 'stead': stead}
