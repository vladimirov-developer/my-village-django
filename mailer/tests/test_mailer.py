from __future__ import with_statement

import os

from django.conf import settings
from django.core import mail
from django.template import Context
from django.test import TestCase

from ..base import Mailer
from .models import Recipient


TESTS_ROOT = os.path.abspath(os.path.dirname(__file__))


class MailerTests(TestCase):

    def setUp(self):
        mail.outbox = []
        self.old_TEMPLATE_DIRS = settings.TEMPLATE_DIRS
        settings.TEMPLATE_DIRS = (
            (os.path.join(TESTS_ROOT, 'templates'),) + settings.TEMPLATE_DIRS)
        self.old_EMAIL_BACKEND = settings.EMAIL_BACKEND
        settings.EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

    def tearDown(self):
        settings.TEMPLATE_DIRS = self.old_TEMPLATE_DIRS
        settings.EMAIL_BACKEND = self.old_EMAIL_BACKEND

    def test_invalid_keyword(self):
        with self.assertRaises(TypeError):
            Mailer(invalid_keyword='foo')

    def test_sender(self):
        mailer = Mailer(sender='john@example.com')
        self.assertEqual(mailer.get_sender(), 'john@example.com')

    def test_recipients_as_list(self):
        mailer = Mailer(recipients=['alex@example.com'])
        self.assertEqual(mailer.get_recipients(), ['alex@example.com'])

    def test_recipients_as_tuple(self):
        mailer = Mailer(recipients=('alex@example.com',))
        self.assertEqual(mailer.get_recipients(), ('alex@example.com',))

    def test_recipients_as_queryset(self):
        Recipient.objects.create(email='alex@example.com')
        mailer = Mailer(recipients=Recipient.objects.values_list('email', flat=True))
        self.assertEqual(list(mailer.get_recipients()), ['alex@example.com'])

        Recipient.objects.create(email='kate@example.com')
        self.assertEqual(list(mailer.get_recipients()), ['alex@example.com', 'kate@example.com'])

    def test_invalid_recipients(self):
        mailer = Mailer(recipients='invalid recipients')
        self.assertEqual(len(mailer.get_recipients()), 0)

    def test_template_name(self):
        mailer = Mailer(template_name='mailer')
        self.assertEqual(mailer.get_template_name(), 'mailer')

    def test_subject_template_name(self):
        mailer = Mailer(template_name='mailer')
        self.assertEqual(mailer.get_subject_template_name(), 'mailer/subject.txt')

    def test_message_template_name(self):
        mailer = Mailer(template_name='mailer')
        self.assertEqual(mailer.get_text_message_template_name(), 'mailer/message.txt')

    def test_subject(self):
        mailer = Mailer(template_name='mailer/tests/without_context_instance')
        self.assertEqual(mailer.get_subject(), 'Email subject')

    def test_subject_with_context_instance(self):
        mailer = Mailer(template_name='mailer/tests/with_context_instance')
        context = Context({'domain': 'example.com'})
        self.assertEqual(mailer.get_subject(context), 'Email from example.com')

    def test_message(self):
        mailer = Mailer(template_name='mailer/tests/without_context_instance')
        self.assertEqual(mailer.get_text_message(), 'Email message\n')

    def test_message_with_context_instance(self):
        mailer = Mailer(template_name='mailer/tests/with_context_instance')
        context = Context({'domain': 'example.com'})
        self.assertEqual(mailer.get_text_message(context), 'Email message from example.com\n')

    def test_context_data(self):
        mailer = Mailer()
        self.assertEqual(mailer.get_context_data(), {})
        self.assertEqual(mailer.get_context_data(domain='example.org'), {'domain': 'example.org'})

        mailer = Mailer(context_data={'domain': 'example.com'})
        self.assertEqual(mailer.get_context_data(), {'domain': 'example.com'})
        self.assertEqual(mailer.get_context_data(domain='example.org'), {'domain': 'example.com'})

    def test_context_instance(self):
        mailer = Mailer(context_data={'domain': 'example.com'})
        context_instance = mailer.get_context_instance()
        self.assertIsInstance(context_instance, Context)
        self.assertIn('domain', context_instance)
        self.assertEqual(context_instance['domain'], 'example.com')

    def test_send_empty_recipients(self):
        Mailer.send(template_name='mailer/tests/without_context_instance')
        self.assertEqual(len(mail.outbox), 0)

    def test_send_with_recipients(self):
        Mailer.send(
            sender = 'kate@example.com',
            recipients = ('alex@example.com', 'john@example.com'),
            template_name = 'mailer/tests/without_context_instance')
        self.assertEqual(len(mail.outbox), 2)

        message = mail.outbox[0]
        to = ('alex@example.com', 'john@example.com')
        for i, message in enumerate(mail.outbox):
            self.assertEqual(message.subject, 'Email subject')
            self.assertEqual(message.body, 'Email message\n')
            self.assertEqual(message.from_email, 'kate@example.com')
            self.assertItemsEqual(message.to, [to[i]])
