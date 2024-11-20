from django.db import models

# Create your models here.
class ProductTable(models.Model):
    username = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class UserTable(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=10, decimal_places=2)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)