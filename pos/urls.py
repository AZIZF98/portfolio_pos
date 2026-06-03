from django.contrib import admin
from django.urls import path
from pos import views


urlpatterns = [
    path('product/', views.products),
    path('product/<int:id>', views.product_update),
    path('product/<int:id>', views.product_delete),
    path('product/<int:id>', views.product_get_detail),

    path('order/', views.orders),
    path('order/<int:id>', views.order_update),
    path('order/<int:id>', views.order_delete),
    path('order/<int:id>', views.order_get_detail),

    path('customer/', views.customers),
    path('customer/<int:id>', views.customer_update),
    path('customer/<int:id>', views.customer_delete),
    path('customer/<int:id>', views.customer_get_detail),
]