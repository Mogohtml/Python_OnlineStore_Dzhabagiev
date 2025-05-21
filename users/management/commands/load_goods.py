from django.core.management.base import BaseCommand
from users.models import Product, Customer, Inventory, Order, ShoppingCart, Category


class Command(BaseCommand):
    help = 'Load goods into the inventory'

    def handle(self, *args, **options):
        # Создание категорий
        category1 = Category.objects.create(name='Гигиена')
        category2 = Category.objects.create(name='Дом')

        # Создание товаров
        product = Product.objects.create(
            name='Полотенце',
            description='Полотенце из микрофибры',
            price=299.99,
            category=category2
        )
        product1 = Product.objects.create(
            name='Зубная паста',
            description='Colgate для полости рта с экстрактом лаванды',
            price=129.99,
            category=category1
        )

        # Создание клиента
        customer = Customer.objects.create(
            last_name='Путин',
            first_name='Владимир',
            patronymic='Владимирович',
            address='г. Ставрополь ул Скандинавская 32 дом 1 квартира 23',
            phone_number='79886789095',
            email='dyadya@vova.com'
        )

        # Создание инвентаря
        inventory = Inventory.objects.create(product=product, quantity=100)
        inventory1 = Inventory.objects.create(product=product1, quantity=200)

        # Создание заказов
        order = Order.objects.create(
            customer=customer,
            product=product1,
            quantity=1,
            status='На рассмотрении'
        )
        order1 = Order.objects.create(
            customer=customer,
            product=product,
            quantity=1,
            status='На рассмотрении'
        )

        # Создание корзины покупок
        shopping_cart = ShoppingCart.objects.create(
            customer=customer,
            product=product1,
            quantity=1
        )
        shopping_cart1 = ShoppingCart.objects.create(
            customer=customer,
            product=product,
            quantity=1
        )

        self.stdout.write(self.style.SUCCESS('Successfully goods loaded'))

