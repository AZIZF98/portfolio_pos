from django.shortcuts import render, get_object_or_404
from rest_framework import status

from pos.models import Product, Order, Customer, Payment
from pos.serializers import ProductSerializer, OrderSerializer, CustomerSerializer, PaymentSerializer
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

@api_view(['GET', 'UPDATE', 'DELETE'])
def product_detail(request, id):
    serializer = ProductSerializer(instance=Product)
    if request.method == 'GET':
        products = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(products)
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

@api_view(['GET', 'UPDATE', 'DELETE'])
def order_get_detail(request, id):
    if request.method == 'GET':
        order = get_object_or_404(Order, pk=id)
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)

    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



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

@api_view(['GET','POST'])
def payments(request):
    if request.method == 'GET':
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)
    data = request.data
    # print(data)
    serializer = PaymentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    print('Testing?')
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

def payments_detail(request):
    return Response()