from django.test import TestCase
from django.urls import reverse, resolve
from ..views import post_form


class TestUrls(TestCase):

    def test_post_form_is_resolved(self):
        url = reverse('post-form')
        self.assertEquals(resolve(url).func, post_form)
