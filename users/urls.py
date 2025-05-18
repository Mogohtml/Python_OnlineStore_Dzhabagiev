from django.urls import path
from users.views import product_list, product_detail, category_list, category_detail, inventory_list, inventory_detail, \
    shopping_cart_list, shopping_cart_detail, order_list, order_detail

urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('categories/', category_list, name='products_list'),
    path('categories/<int:pk>/', category_detail, name='product_detail'),
    path('intentories/', inventory_list, name='inventory_list'),
    path('inventories/<int:pk>/', inventory_detail, name='inventory_detail'),
    path('shopping_cart/', shopping_cart_list, name='shopping_cart_list'),
    path('shopping_cart/<int:pk>/', shopping_cart_detail, name='shopping_cart_detail'),
    path('orders/', order_list, name='order_list'),
    path('orders/<int:pk>/', order_detail, name='order_detail'),
]