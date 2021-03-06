from django.db import models
from django.http import Http404
from django.core.validators import MinValueValidator

class Seller(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

STATUS_PRODUCT = [
    ("A","Active"),
    ("I","Inactive"),
]        
        
class Product(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=200)
    price = models.FloatField()
    stock_quantity = models.IntegerField(validators=[MinValueValidator(0)])
    status = models.CharField(max_length=1, default="A", choices=STATUS_PRODUCT)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

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