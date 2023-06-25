from django.http import HttpRequest
from django.shortcuts import render, redirect
from products.models import Product
from cart.models import Cart
from django.db import transaction


def cart_detail(request: HttpRequest, **kwargs):
    return redirect('my_store_app:cart')


def delete_product(request: HttpRequest, **kwargs):
    with transaction.atomic():
        product = Cart.objects.get(id=kwargs['id'])
        Cart.objects.get(id=kwargs['id']).delete()

        prod_count = Product.objects.get(id=product.product.id)
        count = product.quantity + prod_count.count
        Product.objects.filter(id=product.product.id).update(
            count=count
        )
    return redirect(request.META['HTTP_REFERER'])


def update_product(request: HttpRequest, **kwargs):
    product = Cart.objects.get(id=kwargs['id'])
    old_count = product.quantity
    count = request.POST.get('amount')
    prod_count = Product.objects.get(id=product.product.id)
    if old_count > int(count):
        remove = product.product.count
        new_count = prod_count.count + (old_count - int(count))
    else:
        remove = int(count) - old_count
        new_count = prod_count.count - (int(count) - old_count)
    if product.product.count >= remove:
        with transaction.atomic():

            Cart.objects.filter(id=kwargs['id']).update(
                quantity=count,
            )

            Product.objects.filter(id=product.product.id).update(
                count=new_count
            )

    return redirect(request.META['HTTP_REFERER'])
