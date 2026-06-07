from django.shortcuts import render
from rest_framework import status

from pos.models import Product, Order, Customer
from pos.serializers import ProductSerializer, OrderSerializer, CustomerSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET','POST'])
def products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    data = request.data
    serializer = ProductSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

def product_update(request):
    return Response()
def product_delete(request):
    return Response()
def product_get_detail(request):
    return Response()

@api_view(['GET','POST'])
def orders(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    data =request.data
    serializer = OrderSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

def order_update(request):
    return Response()
def order_delete(request):
    return Response()
def order_get_detail(request):
    return Response()

@api_view(['GET','POST'])
def customers(request):
    if request.method == 'GET':
        customer = Customer.objects.all()
        serializer = CustomerSerializer(customer, many=True)
        return Response(serializer.data)
    data = request.data
    serializer = CustomerSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

def customer_create(request):
    return Response()
def customer_update(request):
    return Response()
def customer_delete(request):
    return Response()
def customer_get_detail(request):
    return Response()