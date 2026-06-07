from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    manufacturing_date = models.DateField()
    notes = models.TextField()

class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('canceled', 'Canceled')
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    transaction_date = models.DateField()
    cashier = models.CharField(max_length=200)
    total = models.FloatField()
    status= models.CharField(max_length=200, choices=STATUS_CHOICES, default='pending')
    invoice_number = models.CharField(max_length=200,default='')


class OrderLine(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='lines')
    quantity = models.IntegerField()
    price = models.FloatField()
    quantity = models.IntegerField()
    price = models.FloatField()
    subtotal = models.FloatField()