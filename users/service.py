from .models import Order, ShoppingCart, Customer, Product, Inventory


def send_order(order_id):
    order = Order.objects.get(pk=order_id)
    if order.status == "На рассмотрении":
        order.status = "Отправлен"
        order.save()
        return True
    return False

def add_to_cart(customer_id, product_id, quantity):
    customer = Customer.objects.get(pk=customer_id)
    product = Product.objects.get(pk=product_id)
    cart, created = ShoppingCart.objects.get_or_create(customer=customer, product=product, defaults={'quantity': 0})
    cart.quantity += quantity
    cart.save()

    inventory = Inventory.objects.get(product=product)
    if inventory.quantity >= quantity:
        inventory.quantity -= quantity
        inventory.save()
        return True
    return False


