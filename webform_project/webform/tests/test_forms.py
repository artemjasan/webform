from django.test import TestCase

from .utils import FormUtils, TextError, DATA_VALID
from ..forms import CreateForm


class TestForms(TestCase):

    def test_create_form_valid_all_data(self):
        form = CreateForm(data=DATA_VALID)
        self.assertTrue(form.is_valid())

    def test_create_form_no_data(self):
        form = CreateForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)
        self.assertEquals(form.errors['name'][0], TextError.FIELD_REQUIRED)
        self.assertEquals(form.errors['ico'][0], TextError.FIELD_REQUIRED)

    def test_create_form_invalid_data_no_name(self):
        form = CreateForm(data=FormUtils.DATA_INVALID_NAME)
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
        self.assertEquals(form.errors['name'][0], TextError.FIELD_REQUIRED)

    def test_create_form_invalid_data_long_name(self):
        form = CreateForm(data=FormUtils.DATA_LONG_NAME)
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
        self.assertEquals(form.errors['name'][0], TextError.NAME_FIELD_LONG)

    def test_create_form_invalid_data_email(self):
        form = CreateForm(data=FormUtils.DATA_INVALID_EMAIL)
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
        self.assertEquals(form.errors['email'][0], TextError.INVALID_EMAIL)

    def test_create_form_invalid_data_no_email(self):
        form = CreateForm(data=FormUtils.DATA_EMAIL_NONE)
        self.assertTrue(form.is_valid())

    def test_create_form_invalid_data_long_email(self):
        form = CreateForm(data=FormUtils.DATA_LONG_EMAIL)
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
        self.assertEquals(form.errors['email'][0], TextError.EMAIL_FIELD_LONG)

    def test_create_form_invalid_data_ico(self):
        form = CreateForm(data=FormUtils.DATA_INVALID_ICO)
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
        self.assertEquals(form.errors['ico'][0], TextError.INVALID_ICO)

    def test_create_form_invalid_data_no_ico(self):
        form = CreateForm(data=FormUtils.DATA_INVALID_ICO_NONE)
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
        self.assertEquals(form.errors['ico'][0], TextError.FIELD_REQUIRED)

    def test_create_form_invalid_data_ico_unique(self):
        form = CreateForm(data=DATA_VALID)
        form.save()
        new_form = CreateForm(data=DATA_VALID)
        self.assertFalse(new_form.is_valid())
        self.assertEquals(len(new_form.errors), 1)
        self.assertEquals(new_form.errors['ico'][0], TextError.FIELD_UNIQUE)

    def test_create_form_invalid_data_long_ico(self):
        form = CreateForm(data=FormUtils.DATA_LONG_ICO)
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
        self.assertEquals(form.errors['ico'][0], TextError.ICO_FIELD_LONG)
