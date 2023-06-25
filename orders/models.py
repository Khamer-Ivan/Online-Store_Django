from django.db import models
from django.contrib.auth.models import User
from my_store_app.models import Profile
from products.models import Product


class OrderHistory(models.Model):  # история покупок пользователя
    user_order = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='пользователь', null=True)
    product_order = models.ForeignKey('products.Product', on_delete=models.CASCADE, verbose_name='товар')
    payment_date = models.DateField(auto_now_add=True)
    delivery_type = models.TextField(max_length=30, default='не указан', verbose_name='способ доставки')
    payment_type = models.TextField(max_length=30, default='не указан', verbose_name='способ оплаты')
    total_cost = models.IntegerField(default=0, verbose_name='общая стоимость заказа')
    status = models.TextField(max_length=30, default='не указан', verbose_name='статус оплаты')
    city = models.TextField(max_length=30, default='не указан', verbose_name='город доставки')
    address = models.TextField(max_length=30, default='не указан', verbose_name='адрес доставки')

    class Meta:
        verbose_name = 'История покупок'
        verbose_name_plural = 'Истории покупок'

    def __str__(self):
        return self.user_order.full_name


class Order(models.Model):  # покупка товаров из корзины

    DELIVERY_CHOICES = [
        ('reg', 'Обычная доставка'),
        ('exp', 'Экспресс доставка')
    ]

    PAYMENT_CHOICES = [
        ('card', 'Онлайн картой'),
        ('cash', 'Онлайн со случайного чужого счета'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='orders', verbose_name='customer')
    fio = models.CharField(max_length=100, null=True, blank=True, verbose_name='name and lastname')
    phone = models.CharField(max_length=16, null=True, blank=True, verbose_name='phone number')
    email = models.EmailField(null=True, blank=True, verbose_name='email')
    delivery = models.CharField(max_length=3, choices=DELIVERY_CHOICES, default='reg', verbose_name='delivery')
    payment_method = models.CharField(max_length=4, choices=PAYMENT_CHOICES, default='card', verbose_name='payment method')
    city = models.CharField(max_length=25, null=True, blank=True, verbose_name='city')
    address = models.TextField(max_length=255, null=True, blank=True, verbose_name='address')
    in_order = models.BooleanField(default=False, verbose_name='in order')
    paid = models.BooleanField(default=False, verbose_name='order is payed')
    braintree_id = models.CharField(max_length=150, blank=True, verbose_name='transaction id')
    delivery_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='delivery cost')
    product_order = models.ForeignKey('products.Product', on_delete=models.CASCADE, null=True, verbose_name='товар', related_name='product_order')
    count = models.IntegerField(default=0, verbose_name='колличество  товаров в корзине')
    price = models.IntegerField(default=0, verbose_name='общая стоимость  товаров в корзине')
    date = models.DateField(auto_now_add=True)
    free_delivery = models.BooleanField(default=False, verbose_name='наличие бесплатной доставки')

    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'

    def __str__(self):
        return self.product_order


class ProductInOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, unique=False, related_name='user')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True, unique=False, related_name='order')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, unique=False, related_name='prod')
    quantity = models.PositiveIntegerField(default=0, null=True)

