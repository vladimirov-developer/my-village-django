# coding: utf-8
from django.shortcuts import render, get_object_or_404
from django.http import Http404, JsonResponse

from mailer_recipients.base import RecipientsMailer

from .models import Queue, Stead
from .forms import OrderForm


def order_view(request, pk=None):
    stead_qs = Stead.objects.filter(status=0)
    stead = get_object_or_404(stead_qs, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.stead = stead
            message.save()
            RecipientsMailer.send(
                request=request,
                object=message,
                template_name='plan/mail',
            )
            return render(request, 'plan/order_form.html', {
                'form': OrderForm(),
                'stead': stead,
                'success': True
            })
    else:
        form = OrderForm()
    return render(request, 'plan/order_form.html', {
        'form': form,
        'stead': stead,
        'success': False
    })


def stead_reservation(request, pk=None):
    stead_qs = Stead.objects.filter(status=0)
    stead = get_object_or_404(stead_qs, pk=pk)
    return render(request, 'plan/reservation.html', {
        'stead': stead,
    })


def general(request):
    try:
        q1 = Queue.objects.filter(queue=1)[0]
    except IndexError:
        q1 = None
    try:
        q2 = Queue.objects.filter(queue=2)[0]
    except IndexError:
        q2 = None
    return render(request, 'plan/general.html', context={'q1': q1, 'q2': q2})


def plan(request, queue):
    obj = get_object_or_404(Queue, queue=queue)
    reserved_steads = Stead.objects.filter(
        queue=obj, status=1
    ).values_list('id_stead', flat=True)
    sold_steads = Stead.objects.filter(
        queue=obj, status=2
    ).values_list('id_stead', flat=True)
    return render(
        request, 'plan/plan_{}.html'.format(queue), context={
            'object': obj,
            'reserved_steads': map(lambda x: str(x), list(reserved_steads)),
            'sold_steads': map(lambda x: str(x), list(sold_steads))
        }
    )


def stead(request, queue, stead_id):
    queue_obj = get_object_or_404(Queue, queue=queue)
    stead_qs = Stead.objects.filter(queue=queue_obj)
    stead_qs = stead_qs.exclude(status__in=[1, 2])
    stead = get_object_or_404(stead_qs, id_stead=stead_id)
    return render(
        request, 'plan/popup.html', context={'object': stead}
    )


def stead_edit(request, queue, stead_id):
    if request.user.is_authenticated():
        if request.user.is_superuser:
            queue_obj = get_object_or_404(Queue, queue=queue)
            stead, _ = Stead.objects.get_or_create(queue=queue_obj, id_stead=stead_id, defaults={
                'number': stead_id.replace('id', ''), 'title': u'Участок №{}'.format(stead_id.replace('id', ''))}
            )
            return JsonResponse(data={'url': '/admin/plan/stead/{}/change/'.format(stead.pk)})
    raise Http404
