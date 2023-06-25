from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from profile.models import Profile


class Cart(models.Model):  # корзина пользователя
    username = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="profile"
    )
    product = models.ForeignKey(
        Product, default=1, on_delete=models.CASCADE, related_name="product"
    )
    quantity = models.PositiveIntegerField(default=0)
    create_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"


class Payment(models.Model):
    number = models.IntegerField(default=0, verbose_name="номер счета")
    name = models.TextField(max_length=30, default="не указан")
    month = models.DateField(auto_now_add=True)
    year = models.DateField(auto_now_add=True)
    code = models.IntegerField(default=0, verbose_name="код оплаты")

    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплата"

    def __str__(self):
        return self.name
