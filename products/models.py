from django.db import models
from django.contrib.auth.models import User
from my_store_app.models import Profile


class Sales(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='товар')
    shop = models.ForeignKey('Shop', on_delete=models.CASCADE, verbose_name='магазин')
    count = models.IntegerField(default=0, verbose_name='количество товара по скидке')
    dateFrom = models.DateField()
    dateTo = models.DateField()

    class Meta:
        verbose_name = 'Распродажа'
        verbose_name_plural = 'Распродажа'


class CategoryProduct(models.Model):  # категория товаров
    title = models.TextField(max_length=50, verbose_name='название категории')
    image = models.FileField(upload_to='my_store_app/static/', null=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Product(models.Model):  # товар
    category = models.ForeignKey('CategoryProduct', on_delete=models.CASCADE, verbose_name='категория товара',
                                 related_name='category')
    shop = models.ForeignKey('Shop', on_delete=models.CASCADE, verbose_name='магазин товара', related_name='shop')
    specifications = models.ForeignKey('Specifications', on_delete=models.CASCADE, verbose_name='спецификация товара')
    price = models.IntegerField(default=0, verbose_name='цена товара')
    count = models.IntegerField(default=0, verbose_name='количество ')
    date = models.DateField(auto_now_add=True)
    title = models.TextField(max_length=50, verbose_name='название товара')
    description = models.TextField(max_length=100, verbose_name='описание товара')
    free_delivery = models.BooleanField(default=True)
    product_picture = models.ImageField(upload_to='my_store_app/static/', null=True)
    rating = models.IntegerField(default=0, verbose_name='счетчик покупок данного товара')
    reviews = models.IntegerField(default=0, verbose_name='счетчик просмотров данного товара')
    tags = models.ManyToManyField('TagsFile', related_name='tags')
    limited_edition = models.BooleanField(default=False, null=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title


class TagsFile(models.Model):
    tags_name = models.TextField(max_length=50, verbose_name='тэг товара')

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.tags_name


class Shop(models.Model):
    shop_name = models.TextField(max_length=50, verbose_name='название магазина')

    class Meta:
        verbose_name = 'магазин'
        verbose_name_plural = 'магазины'

    def __str__(self):
        return self.shop_name


class Reviews(models.Model):  # отзыв
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='товар',
                                related_name='product_title_product_set')
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='пользователь')
    text = models.CharField(default='Не указано', max_length=100, verbose_name='текст отзыва', blank=True)
    create_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.text


class Specifications(models.Model):
    name = models.TextField(max_length=50, verbose_name='название')
    value = models.TextField(max_length=50, verbose_name='значение')

    class Meta:
        verbose_name = 'Спецификация'
        verbose_name_plural = 'Спецификации'

    def __str__(self):
        return self.name
