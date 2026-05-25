from django.shortcuts import render

from pos.models import Product, Order, Customer
from pos.serializers import ProductSerializer, OrderSerializer, CustomerSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def product_get_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

def product_create(request):
    return Response()
def product_update(request):
    return Response()
def product_delete(request):
    return Response()
def product_get_detail(request):
    return Response()

@api_view(['GET'])
def order_list(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)
def order_create(request):
    return Response()
def order_update(request):
    return Response()
def order_delete(request):
    return Response()
def order_get_detail(request):
    return Response()

@api_view(['GET'])
def customer_list(request):
    customer = Customer.objects.all()
    serializer = CustomerSerializer(customer, many=True)
    return Response(serializer.data)
def customer_create(request):
    return Response()
def customer_update(request):
    return Response()
def customer_delete(request):
    return Response()
def customer_get_detail(request):
    return Response()