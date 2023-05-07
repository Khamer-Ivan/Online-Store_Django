from django.http import HttpRequest
from django.shortcuts import render, redirect
from my_store_app.models import Product, Cart


def cart_detail(request: HttpRequest, **kwargs):
    return redirect('my_store_app:cart')


def delete_product(request: HttpRequest, **kwargs):
    Cart.objects.get(id=kwargs['id']).delete()
    return redirect(request.META['HTTP_REFERER'])


def update_product(request: HttpRequest, **kwargs):
    product = Cart.objects.get(id=kwargs['id'])
    count = request.POST.get('amount')

    Cart.objects.filter(id=kwargs['id']).update(
        quantity=count,
    )
    return redirect(request.META['HTTP_REFERER'])
