from django.urls import path
from users.views import register, product_list, product_detail, category_list, category_detail, inventory_list, \
    inventory_detail, \
    shopping_cart_list, shopping_cart_detail, order_list, order_detail, home_view, add_to_cart, create_order
from django.contrib.auth import views as auth_views


urlpatterns = [
path('home/', home_view, name='home'), # Add in paths for user interface
    path('register/', register, name='register'), # Add in paths for user interface
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'), # Add in paths for user interface
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'), # Add in paths for user interface
    path('products/', product_list, name='product_list'), # Add in paths for user interface
    path('products/<int:pk>/', product_detail, name='product_detail'), # Add in paths for user interface
    path('categories/', category_list, name='products_list'), # Add in paths for user interface
    path('categories/<int:pk>/', category_detail, name='product_detail'), # Add in paths for user interface
    path('intentories/', inventory_list, name='inventory_list'), # Add in paths for user interface
    path('inventories/<int:pk>/', inventory_detail, name='inventory_detail'), # Add in paths for user interface
    path('shopping_cart/', shopping_cart_list, name='shopping_cart_list'), # Add in paths for user interface
    path('shopping_cart/<int:pk>/', shopping_cart_detail, name='shopping_cart_detail'), # Add in paths for user interface
    path('shopping_cart/add/', add_to_cart, name='add_to_cart'), # Add in paths for user interface
    path('orders/', order_list, name='order_list'), # Add in paths for user interface
    path('orders/<int:pk>/', order_detail, name='order_detail'), # Add in paths for user interface
    path('orders/arrage/', create_order, name="create_order"), # Add in paths for user interface
]
