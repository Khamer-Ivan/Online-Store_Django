from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from django import template
from django.db import transaction

from cart.forms import CartAddProductForm
from my_store_app.models import Product, CategoryProduct, TagsFile, Cart, Profile

register = template.Library()


class CatalogView(ListView):
    model = Product
    context_object_name = 'catalog'
    template_name = 'products/catalog.html'


class CategoryView(DetailView):
    template_name = 'products/category.html'
    model = CategoryProduct
    context_object_name = 'category'


class ProductView(View):
    def get(self, request: HttpRequest):
        return render(request, 'products/product.html')


class ProductDetail(DetailView):
    template_name = 'products/product.html'
    model = Product
    context_object_name = 'product'


def product_detail(request: HttpRequest, **kwargs):
    if request.method == 'POST':
        product = Product.objects.get(id=kwargs['pk'])
        basket = Cart.objects.filter(username=request.user.profile, product=product)
        with transaction.atomic():
            count = product.count - 1
            Product.objects.filter(id=kwargs['pk']).update(
                count=count
            )

            if not basket.exists():
                Cart.objects.create(
                    username=request.user.profile,
                    product=product,
                    quantity=1
                )
                return redirect('my_store_app:index')

            else:
                cart = basket.first()
                cart.quantity += 1
                cart.save()
                return redirect('my_store_app:index')

    else:
        product = Product.objects.get(id=kwargs['pk'])
    return render(request, 'products/product.html', {'product': product})


class TagView(DetailView):
    template_name = 'products/tag_page.html'
    model = TagsFile
    context_object_name = 'tags'

