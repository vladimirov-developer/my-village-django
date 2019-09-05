from django.test import TestCase
from django.template import RequestContext

from ..base import ModelMailer
from .models import Message


class ModelMixinTests(TestCase):

    def setUp(self):
        self.message = Message.objects.create(full_name='Alex', text='Message')

    def test_object(self):
        mailer = ModelMailer(object=self.message)
        self.assertEqual(mailer.get_object(), self.message)

    def test_model(self):
        mailer = ModelMailer(object=self.message)
        self.assertEqual(mailer.get_model(), Message)

    def test_template_name(self):
        mailer = ModelMailer(object=self.message)
        self.assertEqual(mailer.get_template_name(), 'mailer/mailer/message')

        mailer = ModelMailer(object=self.message, template_name='custom/template/name')
        self.assertEqual(mailer.get_template_name(), 'custom/template/name')

    def test_context_data(self):
        mailer = ModelMailer(object=self.message)
        self.assertEqual(mailer.get_context_data(), {'object': self.message})
