from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User, Product, Category, Customer, Inventory, ShoppingCart, Order

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Inventory)
admin.site.register(ShoppingCart)
admin.site.register(Order)