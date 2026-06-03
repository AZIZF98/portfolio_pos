from http.cookiejar import debug

from django.db import transaction
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
        fields = ['product', 'quantity', 'price', 'subtotal']

class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    customer_id = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    lines = OrderLinerSerializer(many=True)
    class Meta:
        model = Order
        fields = ['id','customer','customer_id','transaction_date', 'cashier', 'total', 'lines']

    @transaction.atomic
    def create(self, validated_data):
        lines = validated_data.pop('lines')
        print(validated_data)

        if validated_data.get('customer_id'):
            validated_data['customer_id'] = validated_data['customer_id'].id
        order = Order.objects.create(**validated_data)

        for line in lines:
            line['order_id'] = order.id
            OrderLine.objects.create(**line)
        print(order)
        return order