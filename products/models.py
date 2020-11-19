from django.db import models
from django.http import Http404

class Seller(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    status_product = [
        ("A", "Active"),
        ("I", "Inactive"),
    ]
    
    code = models.IntegerField()
    name = models.CharField(max_length=200)
    price = models.FloatField()
    stock_quantity = models.IntegerField()
    status = models.CharField(max_length=1, choices=status_product)
    seller = models.ForeignKey(Seller, null=True, on_delete=models.SET_NULL)


    def to_dict(self):
        return {
            "id": self.id,
            "code": self.code,
            "name": self.name,
            "price": self.price,
            "stock_quantity": self.stock_quantity,
            "status": self.status,
            "seller": self.seller.name,
            }

    def __str__(self):
        return self.name