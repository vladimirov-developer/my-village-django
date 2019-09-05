from django.conf import settings
from django.core.mail import EmailMultiAlternatives, get_connection
from django.db.models.query import QuerySet
from django.template import Context, RequestContext
from django.template.loader import render_to_string
from django.template import TemplateDoesNotExist


class Mailer(object):

    sender = None
    recipients = None
    template_name = None
    context_data = None
    fail_silently = False
    attachments = None

    def __init__(self, **kwargs):
        for key, value in kwargs.iteritems():
            if not hasattr(self, key):
                raise TypeError(u'%s() received an invalid keyword %r' % (
                    type(self).__name__, key))
            setattr(self, key, value)

    def get_sender(self):
        return self.sender or settings.DEFAULT_FROM_EMAIL

    def get_recipients(self):
        if isinstance(self.recipients, (list, tuple)):
            return self.recipients
        if isinstance(self.recipients, QuerySet):
            return self.recipients._clone()
        return ()

    def get_template_name(self):
        return self.template_name

    def get_subject_template_name(self):
        return self.get_template_name() + '/subject.txt'

    def get_text_message_template_name(self):
        return self.get_template_name() + '/message.txt'

    def get_html_message_template_name(self):
        return self.get_template_name() + '/message.html'

    def get_subject(self, context_instance=None):
        subject = render_to_string(
            template_name=self.get_subject_template_name(),
            context=context_instance,
        )
        return ''.join(subject.splitlines())

    def get_text_message(self, context_instance=None):
        return render_to_string(
            template_name=self.get_text_message_template_name(),
            context=context_instance,
        )

    def get_html_message(self, context_instance=None):
        try:
            message = render_to_string(
                template_name=self.get_html_message_template_name(),
                context=context_instance,
            )
        except TemplateDoesNotExist:
            message = None
        return message

    def get_context_data(self, **kwargs):
        kwargs.update(self.context_data or {})
        return kwargs

    def get_context_instance(self):
        return Context(self.get_context_data())

    def get_message(self, subject, text, html, from_email, to):
        message = EmailMultiAlternatives(subject, text, from_email, to)
        if html:
            message.attach_alternative(html, 'text/html')
        if isinstance(self.attachments, (list, tuple)):
            for item in self.attachments:
                if isinstance(item, basestring):
                    message.attach_file(item)
                elif isinstance(item, (list, tuple)):
                    message.attach(*item)
                else:
                    raise ValueError('%r: is not tuple or string' % item)
        return message

    def get_connection(self):
        return get_connection(fail_silently=self.fail_silently)

    @classmethod
    def send(cls, **kwargs):
        mailer = cls(**kwargs)
        from_email = mailer.get_sender()
        context_instance = mailer.get_context_instance()
        subject = mailer.get_subject(context_instance)
        text = mailer.get_text_message(context_instance)
        html = mailer.get_html_message(context_instance)

        messages = []
        for recipient in mailer.get_recipients():
            messages.append(mailer.get_message(
                subject=subject,
                text=text,
                html=html,
                from_email=from_email,
                to=[recipient],
            ))
        mailer.get_connection().send_messages(messages)


class RequestMixin(object):

    request = None

    def get_context_instance(self):
        return RequestContext(self.request, self.get_context_data())


class ModelMixin(object):

    object = None

    def get_object(self):
        return self.object

    def get_model(self):
        return type(self.get_object())

    def get_template_name(self):
        if self.template_name:
            return self.template_name
        options = self.get_model()._meta
        return 'mailer/%s/%s' % (options.app_label, options.object_name.lower())

    def get_context_data(self, **kwargs):
        kwargs['object'] = self.get_object()
        return kwargs


class RequestMailer(RequestMixin, Mailer):

    pass


class ModelMailer(ModelMixin, RequestMixin, Mailer):

    pass
