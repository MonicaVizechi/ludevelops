from django.test import TestCase
from .models import Seller, Product
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

    def test_post(self):
        client = APIClient()
        response = client.post('/products/sellers/', {
            "name": "Batman",
        })

        self.assertEqual(response.status_code, 201)
        self.assertEquals(Seller.objects.count(), 2)
        self.assertEquals(Seller.objects.last().name, "Batman")


class ProductViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        seller = Seller.objects.create(name="Jaqueloja")
        Product.objects.create(code=123,name="batman",price=200.00,stock_quantity=40,status="A",seller=seller)
       
    def test_get(self):
        client = APIClient()
        response = client.get('/products/')

        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)

        self.assertEqual(data.get('count'), 1)

        product1 = data.get('results')[0]

        self.assertEqual(product1.get("code"), 123)
        self.assertEqual(product1.get("name"), "batman")
        self.assertEqual(product1.get("price"), 200.00)
        self.assertEqual(product1.get("stock_quantity"), 40)
        self.assertEqual(product1.get("status"), "A")

    def test_post(self):
        client = APIClient()
        response = client.post('/products/', {
            "code": 123,
            "name":"batman",
            "price":200.00,
            "stock_quantity":40,
            "status":"A",
            "seller": "http://testserver/products/sellers/1/"
            })
        product = Product.objects.last()

        self.assertEqual(response.status_code, 201)
        self.assertEquals(Product.objects.count(), 2)
        self.assertEquals(product.code, 123)
        self.assertEquals(product.name, "batman")
        self.assertEquals(product.price, 200.00)
        self.assertEquals(product.stock_quantity, 40)
        self.assertEquals(product.status, "A")
        