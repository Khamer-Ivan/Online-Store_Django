from django import template

from my_store_app.models import Product, CategoryProduct, TagsFile, Cart, Profile, ProductInOrder

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

