from django.test import Client, TestCase

from .utils import DATA_VALID, FormUtils
from ..forms import CreateForm


class TestForms(TestCase):

    def test_create_form_valid_all_data(self):
        form = CreateForm(data=DATA_VALID)
        self.assertTrue(form.is_valid())

    def test_create_form_invalid_all_data(self):
        form = CreateForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)

    def test_create_form_invalid_data_name(self):
        form = CreateForm(data=FormUtils.DATA_INVALID_NAME)
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_create_form_invalid_data_long_name(self):
        form = CreateForm(data=FormUtils.DATA_LONG_NAME)
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_create_form_invalid_data_email(self):
        form = CreateForm(data=FormUtils.DATA_INVALID_EMAIL)
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_create_form_invalid_data_email_none(self):
        form = CreateForm(data=FormUtils.DATA_EMAIL_NONE)
        self.assertTrue(form.is_valid())

    def test_create_form_invalid_data_long_email(self):
        form = CreateForm(data=FormUtils.DATA_LONG_EMAIL)
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_create_form_invalid_data_ico(self):
        form = CreateForm(data=FormUtils.DATA_INVALID_ICO)
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_create_form_invalid_data_ico_none(self):
        form = CreateForm(data=FormUtils.DATA_INVALID_ICO_NONE)
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_create_form_invalid_data_ico_unique(self):
        form = CreateForm(data=DATA_VALID)
        form.save()
        new_form = CreateForm(data=DATA_VALID)
        self.assertFalse(new_form.is_valid())
        self.assertEquals(len(new_form.errors), 1)

    """def test_create_form_invalid_data_long_ico(self):
        form = CreateForm(data=FormUtils.DATA_LONG_ICO)
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
"""
