import json
from django.test import TestCase
from django.test import Client
from django.forms import Form
from django.forms.fields import CharField

class ExampleForm(Form):
        name = CharField(max_length=50, required=True)
        surname = CharField(max_length=100, required=True)


class FormsTestCase(TestCase):

    def setUp(self):
        self.c = Client()

    def test_render_form(self):
        response = self.c.post('/utils/render-form/', data={'class': 'g_utils.tests.ExampleForm' })
        self.assertEqual(response.status_code, 200)
        response = self.c.post('/utils/render-form/', data={'class': 'g_utils.tests.ExampleForm',
                                                            'form_data':json.dumps({'name':'aaaa'}) })
        self.assertEqual(response['content-type'], 'application/json')



