from django.test import TestCase

from .utils import NAME, EMAIL, ICO, MAX_LENGTH, MAX_LENGTH_ICO
from ..models import Form


class TestFormModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Form.objects.create(name=NAME, email=EMAIL, ico=ICO)

    def test_form_exist(self):
        self.assertTrue(Form.objects.filter(name=NAME).exists())

    def test_name_max_length(self):
        form = Form.objects.get(id=1)
        max_length = form._meta.get_field('name').max_length
        self.assertEquals(max_length, MAX_LENGTH)

    def test_email_max_length(self):
        form = Form.objects.get(id=1)
        max_length = form._meta.get_field('email').max_length
        self.assertEquals(max_length, MAX_LENGTH)

    def test_ico_max_length(self):
        form = Form.objects.get(id=1)
        max_length = form._meta.get_field('ico').max_length
        self.assertEquals(max_length, MAX_LENGTH_ICO)
