from django.http import response
from django.test import Client, TestCase

# Create your tests here.
class ProductTests(TestCase):
    def test_product_text(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "name")