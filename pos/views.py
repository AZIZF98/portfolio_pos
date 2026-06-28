from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from pos.models import Product, Order, Customer, Payment, StockOut, StockIn
from pos.serializers import ProductSerializer, OrderSerializer, CustomerSerializer, PaymentSerializer, \
    StockOutSerializer, StockInSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes


# Create your views here.
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
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
    serializer = OrderSerializer(instance=Order)
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

@api_view(['GET', 'UPDATE', 'DELETE'])
def customer_detail(request, id):
    serializer = CustomerSerializer(instance=Customer)
    if request.method == 'GET':
        customers = get_object_or_404(Customer, pk=id)
        serializer = CustomerSerializer(customers)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

@api_view(['GET', 'UPDATE', 'DELETE'])
def payments_detail(request, id):
    serializer = PaymentSerializer(instance=Payment)
    if request.method == 'GET':
        payments = get_object_or_404(Payment, pk=id)
        serializer = PaymentSerializer(payments)
        return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def stockout(request):
    if request.method == 'GET':
        stockout = StockOut.objects.all()
        serializer = StockOutSerializer(stockout, many=True)
        return Response(serializer.data)
    data = request.data
    serializer = StockOutSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def stockin(request):
    if request.method == 'GET':
        stockin = StockIn.objects.all()
        serializer = StockInSerializer(stockin, many=True)
        return Response(serializer.data)
    data = request.data
    serializer = StockInSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def stockin_confirm(request, id):
    serializer = StockInSerializer(instance=StockIn)
    if request.method == 'GET':
        stockin = get_object_or_404(StockIn, pk=id)
        if stockin.status == 'confirmed':
            return Response({'message': 'Dokumen tidak dapat diconfrim '}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        stockin.status = 'confirmed'
        stockin.product.stock += stockin.quantity
        stockin.product.save()
        stockin.save()
        return Response({'message': "Sukses"},status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
