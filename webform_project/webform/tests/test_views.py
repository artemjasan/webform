from django.test import Client, TestCase
from django.urls import reverse

from .utils import DATA_VALID
from ..models import Form


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.form_url = reverse('post-form')

    def test_form_get(self):
        response = self.client.get(self.form_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'webform/create_form.html')

    def test_form_post(self):
        response_post = self.client.post(self.form_url, data=DATA_VALID)
        self.assertEquals(response_post.status_code, 200)
        data = Form.objects.filter(id=1).first().name
        self.assertEquals(data, DATA_VALID.get('name'))

    def test_form_post_nodata(self):
        response_post = self.client.post(self.form_url)
        self.assertEquals(response_post.status_code, 200)
        data = Form.objects.filter(id=1).count()
        self.assertEquals(data, 0)




