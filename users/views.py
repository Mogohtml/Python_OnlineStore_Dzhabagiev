from django.shortcuts import render, redirect
from .models import Product, Category, Customer, Inventory, ShoppingCart, Order
from .forms import CartForm, OrderForm, ProductForm, CategoryForm, CustomerForm, InventoryForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def home_view(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            form = UserCreationForm()
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


# Create your views here.
def product_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "products/product_list.html", context)

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {"product": product}
    return render(request, "products/product_detail.html", context)

def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm()
    return render(request, "products/create_product.html", {"form": form})


def category_list(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "categories/category_list.html", context)

def category_detail(request, pk):
    category = Category.objects.get(pk=pk)
    context = {"category": category}
    return render(request, "categories/category_detail.html", context)

def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("category_list")
    else:
        form = CategoryForm()
    return render(request, "categories/create_category.html", {"form": form})


def customer_list(request):
    customers = Customer.objects.all()
    context = {"customers": customers}
    return render(request, "customers/customer_list.html", context)

def customer_detail(request, pk):
    customer = Customer.objects.get(pk=pk)
    context = {'customer': customer}
    return render(request, 'customers/customer_detail.html', context)

def create_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("customer_list")
    else:
        form = CustomerForm()
    return render(request, "customers/create_customer.html", {"form": form})


def inventory_list(request):
    inventories = Inventory.objects.all()
    context = {"inventories": inventories}
    return render(request, 'inventories/inventory_list.html', context)

def inventory_detail(request, pk):
    inventory = Inventory.objects.get(pk=pk)
    context = {'inventory': inventory}
    return render(request, 'inventories/inventory_detail.html', context)

def create_inventory(request):
    if request.method == "POST":
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inventory_list")
    else:
        form = InventoryForm()
    return render(request, "inventories/create_inventory.html", {"form": form})


def shopping_cart_list(request):
    carts = ShoppingCart.objects.all()
    context = {"shopping_carts": carts}
    return render(request, 'shopping_cart/shopping_cart_list.html', context)

def shopping_cart_detail(request, pk):
    cart = ShoppingCart.objects.get(pk=pk)
    context = {'shopping_cart': cart}
    return render(request , "shopping_cart/shopping_cart_detail.html", context)

def add_to_cart(request):
    if request.method == "POST":
        form = CartForm(request.POST)
        if form.is_valid():
            product = form.cleaned_data['product']
            quantity = form.cleaned_data['quantity']
            customer = form.cleaned_data['customer']
            cart, created = ShoppingCart.objects.get_or_create(customer=customer, product=product)
            cart.quantity = quantity
            cart.save()
            return redirect('shopping_cart_detail', pk=cart.pk)
        else:
            form = CartForm()
    return render(request, "shopping_cart/add_to_cart.html", {"form": form})


def order_list(request):
    orders = Order.objects.all()
    context = {"orders": orders}
    return render(request, "orders/order_list.html", context)

def order_detail(request, pk):
    order = Order.objects.get(pk=pk)
    context = {'order': order}
    return render(request, "orders/order_detail.html", context)

def create_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            customer = form.cleaned_data['customer']
            product = form.cleaned_data['product']
            quantity = form.cleaned_data['quantity']
            order_date = form.cleaned_data['order_date']
            status = form.cleaned_data['status']
            cart = form.cleaned_data['cart']
            order = Order.objects.create(customer=customer, product=product, quantity=quantity, order_date=order_date, status=status)
            return redirect('order_detail', pk=order.pk)
    else:
        form = OrderForm()
    return render(request, "orders/create_order.html",  {"form": form})

