from django.test import TestCase, Client
from django.urls import reverse
from users.models import Category, Customer, ShoppingCart, Inventory, Product, Order
from users.service import send_order, add_to_cart


# Тестовые данные для классов
class TestContent:
    def setUp(self):
        self.client = Client()
        self.customer = Customer.objects.create(
            last_name="Петрович",
            first_name="Петр",
            address="Шоссе Энтузиастов",
            phone_number="+79880897878",
            email="petrov@petr.com"
        )
        self.category = Category.objects.create(name="Test Category")
        self.product = Product.objects.create(
            name="Test Product",
            description="Test Description",
            price=10.00,
            category=self.category
        )
        self.inventory = Inventory.objects.create(
            product=self.product,
            quantity=10
        )
        self.shopping_cart = ShoppingCart.objects.create(
            customer=self.customer,
            product=self.product,
            quantity=3
        )
        self.order = Order.objects.create(
            customer=self.customer,
            product=self.product,
            quantity=2,
            cart=self.shopping_cart
        )


class ProductInteractionTestCase(TestCase, TestContent):
    def setUp(self):
        super().setUp()

    def test_stock_balance(self):
        # Создаем корзину для пользователя
        cart = ShoppingCart.objects.create(customer=self.customer, product=self.product, quantity=0)

        # Эмулируем POST-запрос для добавления товара в корзину
        response = self.client.post(reverse('add_to_cart'), {
            'product_id': self.product.id,
            'quantity': 3
        })

        # Обновляем объект корзины из базы данных
        cart.refresh_from_db()
        self.assertEqual(cart.quantity, 3)

        # Проверяем, что количество товара на складе уменьшилось
        inventory = Inventory.objects.get(pk=self.inventory.pk)
        self.assertEqual(inventory.quantity, 7)

        # Проверяем, что нельзя добавить больше товара, чем есть на складе
        response = self.client.post(reverse('add_to_cart'), {
            'product_id': self.product.id,
            'quantity': 8
        })

        # Обновляем объект корзины из базы данных
        cart.refresh_from_db()
        self.assertEqual(cart.quantity, 3)

        # Проверяем, что количество товара на складе не изменилось
        inventory.refresh_from_db()
        self.assertEqual(inventory.quantity, 7)


class ProductTestCase(TestCase, TestContent):
    def setUp(self):
        super().setUp()

    def test_product_is_not_empty(self):
        self.assertIsNotNone(self.product)
        self.assertIsNotNone(self.product.name)
        self.assertIsNotNone(self.product.description)
        self.assertIsNotNone(self.product.price)
        self.assertIsNotNone(self.product.category)

    def test_product_valid_value(self):
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.description, "Test Description")
        self.assertEqual(self.product.price, 10.00)
        self.assertEqual(self.product.category, self.category)


class OrderTestCase(TestCase, TestContent):
    def setUp(self):
        super().setUp()

    def test_order_arrange(self):
        self.assertEqual(self.order.customer, self.customer)
        self.assertEqual(self.order.product, self.product)
        self.assertEqual(self.order.quantity, 2)
        self.assertEqual(self.order.cart, self.shopping_cart)
        self.assertEqual(self.order.status, "На рассмотрении")

    def test_order_fields(self):
        self.assertIsNotNone(self.order.order_date)
        self.assertEqual(str(self.order), f"{self.customer} {self.product} {self.order.quantity}")

    # Unit test
    def test_send_order(self):
        result = send_order(self.order.id)
        self.assertTrue(result)
        self.order.refresh_from_db()
        self.assertEqual(self.order.status, "Отправлен")

    def test_send_order_already_sent(self):
        self.order.status = "Отправлен"
        self.order.save()
        result = send_order(self.order.id)
        self.assertFalse(result)
        self.order.refresh_from_db()
        self.assertEqual(self.order.status, "Отправлен")



class ShoppingCartTestCase(TestCase, TestContent):
    def setUp(self):
        super().setUp()

    def test_shopping_cart_valid_value(self):
        self.assertEqual(self.shopping_cart.customer, self.customer)
        self.assertEqual(self.shopping_cart.product.name, "Test Product")
        self.assertEqual(self.shopping_cart.product.description, "Test Description")
        self.assertEqual(self.shopping_cart.product.price, 10.00)
        self.assertEqual(self.shopping_cart.quantity, 3)

    def test_shopping_cart_is_not_empty(self):
        self.assertIsNotNone(self.shopping_cart.customer)
        self.assertIsNotNone(self.shopping_cart.product)
        self.assertIsNotNone(self.shopping_cart.quantity)

    # Unit test
    def test_add_to_cart(self):
        result = add_to_cart(self.customer.id, self.product.id, 3)
        self.assertTrue(result)
        cart = ShoppingCart.objects.get(customer=self.customer, product=self.product)
        self.assertEqual(cart.quantity, 3)
        self.inventory.refresh_from_db()
        self.assertEqual(self.inventory.quantity, 7)

    def test_add_to_cart_not_enough_quantity(self):
        result = add_to_cart(self.customer.id, self.product.id, 15)
        self.assertFalse(result)
        cart = ShoppingCart.objects.get(customer=self.customer, product=self.product)
        self.assertEqual(cart.quantity, 0)
        self.inventory.refresh_from_db()
        self.assertEqual(self.inventory.quantity, 10)

class CustomerTestCase(TestCase, TestContent):
    def setUp(self):
        super().setUp()

    def test_customer_is_not_empty(self):
        self.assertIsNotNone(self.customer)
        self.assertIsNotNone(self.customer.last_name)
        self.assertIsNotNone(self.customer.first_name)
        self.assertIsNotNone(self.customer.patronymic)
        self.assertIsNotNone(self.customer.phone_number)
        self.assertIsNotNone(self.customer.email)

    def test_customer_valid_value(self):
        self.assertEqual(self.customer.last_name, "Петрович")
        self.assertEqual(self.customer.first_name, "Петр")
        self.assertEqual(self.customer.address, "Шоссе Энтузиастов")
        self.assertEqual(self.customer.phone_number, "+79880897878")
        self.assertEqual(self.customer.email, "petrov@petr.com")
