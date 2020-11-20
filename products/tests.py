from django.test import TestCase
from .models import Seller
from rest_framework.test import APIClient
import json

class SellerViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Seller.objects.create(name="Jaqueloja")

    def test_get(self):
        client = APIClient()
        response = client.get('/products/sellers/')

        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)

        self.assertEqual(data.get('count'), 1)

        seller1 = data.get('results')[0]

        self.assertEqual(seller1.get("name"), "Jaqueloja")
