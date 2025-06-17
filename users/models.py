from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(upload_to="products/", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
      return self.name


class Customer(models.Model):
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

class Inventory(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return f"{self.product} {self.quantity}"

class ShoppingCart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1)], default=1)

    def __str__(self):
        return f"{self.customer} {self.product} {self.quantity}"

    def add_item(self, quantity):
        self.quantity += quantity
        self.save()

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default="На рассмотрении")
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return f"{self.customer} {self.product} {self.quantity}"


