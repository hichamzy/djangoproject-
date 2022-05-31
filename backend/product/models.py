from decimal import Decimal
from unicodedata import decimal
from django.db import models

# Create your models here.

class Product(models.Model):
    title=models.TextField(max_length=120)
    content=models.TextField(blank=True,null=True)
    price=models.DecimalField(max_digits=15,decimal_places=2,default=0.0)

    @property
    def seler_price(self):
        return float(self.price*2)
    
    def get_discount(self):
        return 170