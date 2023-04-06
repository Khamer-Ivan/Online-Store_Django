from django import template

from my_store_app.models import Product, CategoryProduct, TagsFile


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

