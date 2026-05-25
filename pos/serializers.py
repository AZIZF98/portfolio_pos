from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class OrderLinerSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderLine
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    lines = OrderLinerSerializer(many=True)
    class Meta:
        model = Order
        fields = ['customer', 'transaction_date', 'cashier', 'total', 'lines']