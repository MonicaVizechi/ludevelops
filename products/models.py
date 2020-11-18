from django.db import models
from django.http import Http404

class Seller(models.Model):
    seller_id = models.IntegerField()
    name = models.CharField(max_length=200)
    
    def __int__(self):
        return self.seller_id

status_product = [
    ("A", "Active"),
    ("I", "Inactive"),
]

class Product(models.Model):
    
    product_id = models.IntegerField()
    name = models.CharField(max_length=200)
    price = models.FloatField()
    stock_quantity = models.IntegerField()
    status = models.CharField(max_length=1, choices=status_product)
    seller = models.ForeignKey(Seller, null=True, on_delete=models.SET_NULL)


    def to_dict(self):
        return {
            "id": self.id,
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "stock_quantity": self.stock_quantity,
            "status": self.status,
            "seller": self.seller.name,
            }

    def __str__(self):
        return self.name