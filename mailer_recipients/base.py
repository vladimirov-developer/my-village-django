from django.contrib.contenttypes.models import ContentType
from mailer import ModelMailer
from .models import Recipient


class RecipientsMixin(object):

    def get_content_type(self):
        return ContentType.objects.get_for_model(self.get_model())

    def get_recipients(self):
        queryset = Recipient.objects.filter(content_type=self.get_content_type())
        return queryset.values_list('email', flat=True)


class RecipientsMailer(RecipientsMixin, ModelMailer):

    pass
