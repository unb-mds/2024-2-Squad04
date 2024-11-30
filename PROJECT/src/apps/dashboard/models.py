from django.db import models
from django.contrib.auth.hashers import make_password


# Create your models here.
class ProductTable(models.Model):
    username = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.IntegerField()

class UserTable(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)

# Function to protect the password
    def save(self, *args, **kwargs):
        if not self.pk:  # Apenas ao criar um novo usuário
            self.password = make_password(self.password)
        super().save(*args, **kwargs)