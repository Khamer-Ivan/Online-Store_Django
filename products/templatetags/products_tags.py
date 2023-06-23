from django import template
from django.http import HttpRequest

from my_store_app.models import Product, CategoryProduct, TagsFile, Cart, Profile, ProductInOrder, Reviews

register = template.Library()


@register.simple_tag()
def product_by_tags(**kwargs):
    tag = kwargs['pk']
    return Product.objects.filter(tags=tag)


@register.simple_tag()
def all_category():
    return CategoryProduct.objects.all()


@register.simple_tag()
def all_tags():
    return TagsFile.objects.all()


@register.simple_tag()
def cart_products(**kwargs):
    if not kwargs['pk']:
        return 0
    cart = Cart.objects.filter(username=kwargs['pk'])
    count = 0
    for product in cart:
        count += product.quantity
    return count


@register.simple_tag()
def cart_total_price(**kwargs):
    if not kwargs['pk']:
        return 0
    cart = Cart.objects.filter(username=kwargs['pk'])
    total_price = 0
    for product in cart:
        total_price += product.product.price * product.quantity

    answer = f'{total_price:,}'
    return answer


@register.simple_tag()
def cart_list(**kwargs):
    if not kwargs['pk']:
        return {}
    return Cart.objects.filter(username=kwargs['pk'])


@register.simple_tag()
def cart_view(**kwargs):
    if not kwargs['pk']:
        return 666

    return kwargs['pk']


@register.simple_tag()
def order_user(**kwargs):
    user = Profile.objects.get(user=kwargs['pk'])
    return user


@register.simple_tag()
def product_in_order(**kwargs):
    if not kwargs['pk']:
        return {}
    return ProductInOrder.objects.filter(user=kwargs['pk'])


@register.simple_tag()
def product_in_order_2(**kwargs):
    if not kwargs['pk']:
        return {}
    return ProductInOrder.objects.filter(order=kwargs['pk'])


@register.simple_tag()
def all_reviews(**kwargs):
    if not kwargs['pk']:
        return {}
    return Reviews.objects.filter(product=kwargs['pk'])


@register.simple_tag()
def reviews_count(**kwargs):
    if not kwargs['pk']:
        return {}
    products = Reviews.objects.filter(product=kwargs['pk'])

    count = 0
    for product in products:
        count += 1

    return count


@register.simple_tag()
def limited_product():
    return Product.objects.filter(limited_edition=1)


@register.simple_tag()
def catalog_query(**kwargs):
    return Product.objects.filter(title__contains=kwargs['pk'])


@register.simple_tag()
def order_by_price():
    product = Product.objects.all()
    high_price = product.order_by('price')
    low_price = product.select_related('-price')
    answer = {'high_price': high_price, 'low_price': low_price}
    return answer


@register.simple_tag()
def most_popular_products():
    product = Product.objects.all()
    return product.order_by('-reviews')[:8]


@register.simple_tag()
def limited_offer():
    product = Product.objects.all()
    return product.order_by('count')[:7]


@register.simple_tag()
def best_rating():
    product = Product.objects.all().order_by('-rating')
    return product.first()



