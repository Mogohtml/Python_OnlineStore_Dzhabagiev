from django import forms
from .models import Product, Customer, ShoppingCart, Category, Inventory, Order
import datetime


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'category']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['last_name', 'first_name', 'patronymic', 'address', 'phone_number', 'email']


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['product', 'quantity']


class CartForm(forms.ModelForm):
    class Meta:
        model = ShoppingCart
        fields = ['customer', 'product', 'quantity']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'product', 'quantity', 'cart']
