from django import forms
from .models import Product, Customer, ShoppingCart, Category, Inventory


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'image', 'category']


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


class CartForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    quantity = forms.IntegerField(min_value=1)
    customer = forms.ModelChoiceField(queryset=Customer.objects.all())


class OrderForm(forms.Form):
    customer = forms.ModelChoiceField(queryset=Customer.objects.all())
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    quantity = forms.IntegerField(min_value=1)
    order_date = forms.DateTimeField(auto_now_add=True)
    status = forms.CharField(max_length=50)
    cart = forms.ModelChoiceField(queryset=ShoppingCart.objects.all())


