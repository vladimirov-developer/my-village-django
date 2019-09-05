from django.test import TestCase, RequestFactory
from django.template import RequestContext

from ..base import RequestMailer


class RequestMixinTests(TestCase):

    def test_context_instance(self):
        mailer = RequestMailer(
            request = RequestFactory().get('/'),
            context_data = {'domain': 'example.com'})
        context_instance = mailer.get_context_instance()
        self.assertIsInstance(context_instance, RequestContext)
        self.assertIn('domain', context_instance)
        self.assertEqual(context_instance['domain'], 'example.com')
