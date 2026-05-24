from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    manufacturing_date = models.IntegerField()
    notes = models.TextField()

class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()

class PostOrder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    transaction_date = models.DateField()
    cashier = models.CharField(max_length=200)