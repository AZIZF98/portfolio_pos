import uuid
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
        fields = [
            'id',
            'customer',
            'customer_id',
            'transaction_date',
            'cashier',
            'total',
            'lines',
            'invoice_number',
            'status'
        ]

    @transaction.atomic
    def create(self, validated_data):
        lines = validated_data.pop('lines')
        print(validated_data)

        if validated_data.get('customer_id'):
            validated_data['customer_id'] = validated_data['customer_id'].id
        validated_data['invoice_number'] = f"INV-{uuid.uuid4().hex[:8]}".upper()
        order = Order.objects.create(**validated_data)

        for line in lines:
            line['order_id'] = order.id
            OrderLine.objects.create(**line)
        print(order)
        return order



class StockOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockOut
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)
    order_id = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())

    class Meta:
        model = Payment
        fields = [
            'id',
            'order_id',
            'order',
            'payment_date',
            'payment_method',
            'paid_amount',
            'change_amount',
        ]

    @transaction.atomic
    def create(self, validated_data):
        if validated_data.get('order_id'):
            for line in validated_data['order_id'].lines.all():
                line_data = {
                    'order_id' : validated_data['order_id'].id,
                    'product_id' : line.product_id,
                    'quantity'  : line.quantity,
                    'transaction_date' : validated_data['payment_date']
                }
                line.product.stock -= line.quantity
                line.product.save()
                StockOut.objects.create(**line_data)

            validated_data['order_id'].status = 'Paid'
            validated_data['order_id'].save()
            validated_data['order_id'] = validated_data['order_id'].id

        return Payment.objects.create(**validated_data)

class StockInSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    class Meta:
        model = StockIn
        fields = [
            'id',
            'product_id',
            'product',
            'quantity',
            'transaction_date',
            'status',
        ]

    @transaction.atomic
    def create(self, validated_data):
        if validated_data.get('product_id'):
            validated_data['product_id'] = validated_data['product_id'].id

        return StockIn.objects.create(**validated_data)


