from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('product/', views.product_get_list),
    path('product/', views.product_create),
    path('product/<int:id>', views.product_update),
    path('product/<int:id>', views.product_delete),
    path('product/<int:id>', views.product_get_detail),

    path('order/', views.order_list),
    path('order/', views.order_create),
    path('order/<int:id>', views.order_update),
    path('order/<int:id>', views.order_delete),
    path('order/<int:id>', views.order_get_detail),

    path('customer/', views.customer_list),
    path('customer/', views.customer_create),
    path('customer/<int:id>', views.customer_update),
    path('customer/<int:id>', views.customer_delete),
    path('customer/<int:id>', views.customer_get_detail),
]