from django.contrib import admin
from django.urls import path
from pos import views


urlpatterns = [
    path('product/', views.products),
    path('product/<int:id>', views.product_detail),


    path('order/', views.orders),
    path('order/<int:id>', views.order_get_detail),


    path('customer/', views.customers),
    path('customer/<int:id>', views.customer_detail),


    path('payment/', views.payments),
    path('payment/<int:id>', views.payments_detail),

    path('stockout/', views.stockout),


    path('stockin/', views.stockin),
    path('stockin/<int:id>/confirm', views.stockin_confirm),
]