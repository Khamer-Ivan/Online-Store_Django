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
    print('=' * 50)
    print(count)
    print('=' * 50)
    Cart.objects.filter(id=kwargs['id']).update(
        quantity=8,
    )
    return redirect(request.META['HTTP_REFERER'])

